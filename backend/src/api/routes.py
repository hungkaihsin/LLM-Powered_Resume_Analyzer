from flask import Blueprint, request, jsonify
import os
import re
from src.api.models.scrapper import (
    scrape_adzuna_jobs,
    parse_resume_pdf,
    extract_skills_from_resume,
    extract_skills_from_job,
    compare_skills,
    safe_extract_skills,
    search_courses_via_serper
)


api_blueprint = Blueprint("api", __name__)

def normalize_skill_query(skill: str) -> str:
    skill = re.sub(r"\(.*?\)", "", skill)
    return skill.strip().lower()

@api_blueprint.route("/analyze", methods=["POST"])
def analyze_resume():
    file = request.files.get("resume")
    keyword = request.form.get("keyword", "machine learning")

    if not file:
        return jsonify({"error": "No resume uploaded"}), 400

    # Save uploaded resume
    filepath = os.path.join("src/data", "Resume.pdf")
    file.save(filepath)

    # Run analysis
    scraped_jobs = scrape_adzuna_jobs(keyword)
    resume_text = parse_resume_pdf(filepath)
    resume_skills_text = extract_skills_from_resume(resume_text)
    resume_skills = safe_extract_skills(resume_skills_text)

    job_results = []
    all_missing_skills = set()

    for job in scraped_jobs:
        job_skills_text = extract_skills_from_job(job["description"])
        job_skills = safe_extract_skills(job_skills_text)
        result = compare_skills(resume_skills, job_skills)
        all_missing_skills.update(result["missing_skills"])

        job_results.append({
            "title": job["title"],
            "company": job["company"],
            "match_percent": result["match_percent"],
            "matched_skills": result["matched_skills"],
            "missing_skills": result["missing_skills"],
            "url": job["url"]
        })

    course_recommendations = []
    for skill in all_missing_skills:
        query = normalize_skill_query(skill)
        courses = search_courses_via_serper(query)
        course_recommendations.append({
            "skill": skill,
            "courses": courses
        })

    return jsonify({
        "resume_skills": resume_skills,
        "jobs": job_results,
        "recommended_courses": course_recommendations
    })
