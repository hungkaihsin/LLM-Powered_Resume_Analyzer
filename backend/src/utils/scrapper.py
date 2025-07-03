import requests
from src.utils.tools import save_jsonl
from pdfminer.high_level import extract_text
import os
from fuzzywuzzy import fuzz
import json
import re
from bs4 import BeautifulSoup


# Mock function for local development
def scrape_adzuna_jobs(keyword: str, location="USA", max_results=2):
    mock_jobs = [
        {
            "title": f"Software Engineer - {keyword}",
            "company": "MockTech Inc.",
            "description": f"Develop software using Python, JavaScript, and cloud technologies. Experience with {keyword} is a plus. Strong knowledge of **GoLang** and **Kubernetes** required.",
            "location": "Remote",
            "url": "https://example.com/mockjob1"
        },
        {
            "title": f"Data Scientist - {keyword} Focus",
            "company": "DataGenius Corp.",
            "description": f"Analyze large datasets, build machine learning models, and work with {keyword} tools. SQL and Python required.",
            "location": "New York, NY",
            "url": "https://example.com/mockjob2"
        },
        {
            "title": f"AI Researcher - {keyword} Applications",
            "company": "FutureLabs",
            "description": f"Research and develop AI solutions, focusing on {keyword} applications. Strong background in algorithms and data structures.",
            "location": "San Francisco, CA",
            "url": "https://example.com/mockjob3"
        },
    ]
    # Filter based on keyword if needed, or just return a subset
    return mock_jobs[:max_results]


# For extract the text froms pdf
def parse_resume_pdf(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError("Resume file not found.")
    
    text = extract_text(file_path)
    return text.strip()


# Mock functions for local development (replacing Gemini API calls)
def extract_skills_from_resume(resume_text: str):
    # Simple keyword-based extraction for local demo
    known_skills = ["Python", "JavaScript", "SQL", "Machine Learning", "Data Analysis", "React", "Flask", "AWS", "Docker", "Git", "Communication", "Problem Solving"]
    extracted = [skill for skill in known_skills if skill.lower() in resume_text.lower()]
    return json.dumps({"skills": extracted})

def extract_skills_from_job(job_description: str):
    # Simple keyword-based extraction for local demo
    known_skills = ["Python", "JavaScript", "SQL", "Machine Learning", "Data Analysis", "React", "Flask", "AWS", "Docker", "Git", "Communication", "Problem Solving", "Leadership", "Agile", "GoLang", "Kubernetes"]
    extracted = [skill for skill in known_skills if skill.lower() in job_description.lower()]
    return json.dumps({"skills": extracted})



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
        extracted_skills = data.get("skills", [])
        return extracted_skills
    except json.JSONDecodeError:
        print("❌ Failed to parse Gemini response as JSON:")
        print(response_text)
        return []
    

# Mock function for local development (replacing Serper API call)
def search_courses_via_serper(skill: str, max_results=2):
    mock_courses = {
        "Python": [
            {"title": "Python for Everybody", "url": "https://www.coursera.org/learn/python"},
            {"title": "Applied Data Science with Python", "url": "https://www.coursera.org/specializations/data-science-python"}
        ],
        "Machine Learning": [
            {"title": "Machine Learning by Andrew Ng", "url": "https://www.coursera.org/learn/machine-learning"},
            {"title": "Deep Learning Specialization", "url": "https://www.coursera.org/specializations/deep-learning"}
        ],
        "JavaScript": [
            {"title": "JavaScript Basics", "url": "https://www.coursera.org/learn/javascript-basics"},
            {"title": "React Basics", "url": "https://www.coursera.org/learn/react-basics"}
        ],
        "SQL": [
            {"title": "SQL for Data Science", "url": "https://www.coursera.org/learn/sql-for-data-science"},
            {"title": "Advanced SQL", "url": "https://www.coursera.org/learn/advanced-sql"}
        ]
    }
    
    # Return courses for the requested skill, or a generic set if not found
    courses = mock_courses.get(skill, [{"title": f"Generic Course for {skill}", "url": "https://www.coursera.org/courses"}])
    return courses[:max_results]