import requests
from src.api.models.tools import ADZUNA_API_KEY, ADZUNA_APP_ID


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

    return jobs
