import requests
from bs4 import BeautifulSoup

def scrape_indeed_jobs(keyword: str, location: str = "remote", max_results=5):
    query = keyword.replace(" ", "+")
    url = f"https://www.indeed.com/jobs?q={query}&l={location}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/113 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []
    cards = soup.select("a.tapItem")

    for card in cards[:max_results]:
        title_tag = card.select_one("h2 span")
        company_tag = card.select_one(".companyName")

        title = title_tag.text.strip() if title_tag else "No title"
        company = company_tag.text.strip() if company_tag else "Unknown"
        link = "https://www.indeed.com" + card["href"]

        jobs.append({
            "title": title,
            "company": company,
            "url": link
        })

    return jobs
