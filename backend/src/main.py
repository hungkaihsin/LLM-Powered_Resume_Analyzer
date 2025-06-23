from src.job_title_generator import generate_titles_and_keywords_gemini
import google.generativeai as genai
from src.job_scraper import scrape_indeed_jobs
from src.utils import save_jsonl 





if __name__ == "__main__":

    # Test generate title from gemini
    # title = generate_titles_and_keywords_gemini("Machine learning engineer in healthcare")
    # print(title)

    jobs = scrape_indeed_jobs("data scientist")
    save_jsonl("src/data/raw_jobs.jsonl", jobs)
    for job in jobs:
        print(job)