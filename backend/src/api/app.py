import json
import re
from src.api.models.scrapper import (
    scrape_adzuna_jobs,
    parse_resume_pdf,
    extract_skills_from_resume,
    extract_skills_from_job,
    compare_skills,
    safe_extract_skills,
    search_coursera_courses  # ✅ new import
)

if __name__ == "__main__":
    print("🔍 Scraping jobs from Adzuna...")
    scraped_jobs = scrape_adzuna_jobs("Machine Learning")  # You can change the keyword

    print("📄 Parsing resume...")
    resume_text = parse_resume_pdf("src/data/Resume.pdf")

    print("🤖 Extracting skills from resume using Gemini...")
    resume_skills_text = extract_skills_from_resume(resume_text)
    resume_skills = safe_extract_skills(resume_skills_text)

    print(f"✅ Resume skills: {resume_skills}\n")

    print("📊 Comparing resume with job listings...\n")
    all_missing_skills = set()

    for idx, job in enumerate(scraped_jobs, start=1):
        print(f"--- Job {idx}: {job['title']} at {job['company']} ---")

        job_skills_text = extract_skills_from_job(job["description"])
        job_skills = safe_extract_skills(job_skills_text)

        result = compare_skills(resume_skills, job_skills)
        all_missing_skills.update(result["missing_skills"])

        print(f"Match: {result['match_percent']}%")
        print(f"Matched Skills: {result['matched_skills']}")
        print(f"Missing Skills: {result['missing_skills']}")
        print("-" * 50)

    print("\n🎓 Recommending Courses for Missing Skills:\n")
    for skill in all_missing_skills:
        print(f"🔧 Skill: {skill}")
        courses = search_coursera_courses(skill)
        if not courses:
            print("  ❌ No courses found.")
        for course in courses:
            print(f"  📘 {course['title']}")
            print(f"     👉 {course['url']}")
        print("-" * 50)