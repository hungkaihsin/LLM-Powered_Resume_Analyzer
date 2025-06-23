from src.api.models.scrapper import scrape_adzuna_jobs
from src.api.models.tools import save_jsonl





if __name__ == "__main__":

    jobs = scrape_adzuna_jobs("data science")
    save_jsonl("src/data/raw_jobs.jsonl", jobs)
    for job in jobs:
        print(job)


