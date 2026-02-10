import requests
from src.utils.tools import save_jsonl
from pdfminer.high_level import extract_text
import google.generativeai as genai
import os
from fuzzywuzzy import fuzz
import json
import re
from bs4 import BeautifulSoup
from src.config import GEMINI_API_KEY, ADZUNA_APP_ID, ADZUNA_API_KEY



# scrape the data from aduza by using its api
def scrape_adzuna_jobs(keyword: str, location="USA", max_results=5):

    url = f"https://api.adzuna.com/v1/api/jobs/us/search/1"
    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_API_KEY,
        "results_per_page": max_results,
        "what": keyword,
        "where": location,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []
    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "description": job.get("description"),
            "location": job.get("location", {}).get("display_name"),
            "url": job.get("redirect_url")
        })
    
    save_jsonl('/tmp/raw_jobs.jsonl', jobs)
    return jobs


# For extract the text froms pdf
def parse_resume_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file not found.")
    
    text = extract_text(file_path)
    return text.strip()


# Allow gemini to extract sthe skill from reusme

if not GEMINI_API_KEY:
    print("WARNING: GEMINI_API_KEY is not set in environment variables!")

genai.configure(api_key=GEMINI_API_KEY, transport='rest')

def extract_skills_from_resume(resume_text: str):
    print(f"DEBUG: Starting Gemini extraction. Text length: {len(resume_text)}")
    if not GEMINI_API_KEY:
        print("ERROR: GEMINI_API_KEY is missing!")
        return json.dumps({"skills": [], "error": "Missing API Key"})

    prompt = f"""
    The following is a resume. Extract a list of professional and technical skills mentioned in it.
    Resume:
    ---
    {resume_text}
    ---
    Return the result in JSON format: {{"skills": ["Skill1", "Skill2"]}}
    """
    
    try:
        print("DEBUG: Calling Gemini API for resume...")
        model = genai.GenerativeModel("gemini-flash-latest")
        
        # Simple retry for quota
        for attempt in range(2):
            try:
                response = model.generate_content(
                    prompt, 
                    generation_config={"response_mime_type": "application/json"}
                )
                return response.text
            except Exception as e:
                if "429" in str(e) and attempt < 1:
                    import time
                    time.sleep(2)
                    continue
                raise e
    except Exception as e:
        print(f"ERROR during Gemini API call: {str(e)}")
        return json.dumps({"skills": [], "error": str(e)})


def extract_skills_from_job(job_description: str):
    if not GEMINI_API_KEY:
        return json.dumps({"skills": []})
        
    prompt = f"""
    The following is a job description. Extract a list of skills or tools required for the role.
    Job Description:
    ---
    {job_description}
    ---
    Return in JSON format: {{"skills": [...]}}
    """
    try:
        model = genai.GenerativeModel("gemini-flash-latest")
        for attempt in range(2):
            try:
                response = model.generate_content(
                    prompt,
                    generation_config={"response_mime_type": "application/json"}
                )
                return response.text
            except Exception as e:
                if "429" in str(e) and attempt < 1:
                    import time
                    time.sleep(2)
                    continue
                raise e
    except Exception as e:
        print(f"ERROR during Gemini Job API call: {str(e)}")
        return json.dumps({"skills": []})




def compare_skills(resume_skills: list, job_skills: list, threshold=80):
    matched = []
    missing = []

    resume_skills_lower = [s.lower() for s in resume_skills]

    for job_skill in job_skills:
        job_skill_lower = job_skill.lower()
        scores = [fuzz.token_set_ratio(job_skill_lower, res) for res in resume_skills_lower]
        best_score = max(scores) if scores else 0

        if best_score >= threshold:
            matched.append(job_skill)
        else:
            missing.append(job_skill)

    match_percent = round((len(matched) / len(job_skills)) * 100) if job_skills else 0
    return {
        "match_percent": match_percent,
        "matched_skills": matched,
        "missing_skills": missing
    }
    
    
    
def safe_extract_skills(response_text):
    """
    Cleans and parses Gemini response to extract the 'skills' list from JSON.
    """
    try:
        # Remove triple backticks and optional 'json' label
        cleaned_text = re.sub(r"```json|```", "", response_text).strip()

        # Load JSON
        data = json.loads(cleaned_text)
        return data.get("skills", [])
    except json.JSONDecodeError:
        print("❌ Failed to parse Gemini response as JSON:")
        print(response_text)
        return []
    


def search_courses_via_serper(skill: str, max_results=3):
    """
    Uses Serper.dev's Google Search API to find relevant Coursera courses for a given skill.
    """
    import os
    import requests
    from src.config import SERPAPI_API_KEY

    if not SERPAPI_API_KEY:
        print("WARNING: SERPAPI_API_KEY is missing!")
        return []

    headers = {
        "X-API-KEY": SERPAPI_API_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "q": f"site:coursera.org {skill}",
        "num": max_results
    }

    response = requests.post("https://google.serper.dev/search", headers=headers, json=data)

    if response.status_code != 200:
        print(f"❌ Serper error {response.status_code}: {response.text}")
        return []

    results = []
    for item in response.json().get("organic", [])[:max_results]:
        results.append({
            "skill": skill,
            "title": item.get("title"),
            "url": item.get("link")
        })

    return results