import requests
from src.api.models.tools import ADZUNA_API_KEY, ADZUNA_APP_ID
from pdfminer.high_level import extract_text
import google.generativeai as genai
import os
from src.api.models.tools import save_jsonl
from dotenv import load_dotenv
from fuzzywuzzy import fuzz
load_dotenv()




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
    
    save_jsonl('src/data/raw_jobs.jsonl', jobs)
    return jobs


# For extract the text froms pdf
def parse_resume_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file not found.")
    
    text = extract_text(file_path)
    return text.strip()


# Allow gemini to extract sthe skill from reusme
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


def extract_skills_from_resume(resume_text: str):
    prompt = f"""
    The following is a resume. Extract a list of **professional and technical skills** mentioned in it.

    Resume:
    ---
    {resume_text}
    ---

    Return the result in JSON format like this:
    {{
        "skills": ["Python", "Machine Learning", "Data Analysis"]
    }}
    """

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text


def extract_skills_from_job(job_description: str):
    prompt = f"""
    The following is a job description. Extract a list of skills or tools required for the role.

    Job Description:
    ---
    {job_description}
    ---

    Return in JSON format:
    {{
        "skills": [...]
    }}
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text




def compare_skills(resume_skills: list, job_skills: list, threshold=80):
    matched = []
    missing = []

    resume_skills_lower = [s.lower() for s in resume_skills]

    for job_skill in job_skills:
        job_skill_lower = job_skill.lower()
        best_match = max([fuzz.token_set_ratio(job_skill_lower, res) for res in resume_skills_lower], default=0)

        if best_match >= threshold:
            matched.append(job_skill)
        else:
            missing.append(job_skill)

    match_percent = int(len(matched) / len(job_skills) * 100) if job_skills else 0

    return {
        "match_percent": match_percent,
        "matched_skills": matched,
        "missing_skills": missing
    }
    