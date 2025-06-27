import requests
import os
from dotenv import load_dotenv

load_dotenv()

def search_courses_via_serpapi(skill: str, max_results=3):
    SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
    print(f"🔑 Using API key: {SERPAPI_KEY}")

    if not SERPAPI_KEY:
        raise ValueError("Missing SERPAPI_API_KEY in environment variables.")

    params = {
        "engine": "google",
        "q": f"site:coursera.org {skill}",
        "api_key": SERPAPI_KEY
    }

    response = requests.get("https://serpapi.com/search", params=params)

    try:
        data = response.json()
    except Exception as e:
        print("❌ JSON parse error:", e)
        print("Raw response:", response.text)
        return []

    if "error" in data:
        print(f"❌ API error: {data['error']}")
        return []

    print("✅ Raw results received:")
    print(data.get("organic_results", []))

    results = []
    for result in data.get("organic_results", [])[:max_results]:
        results.append({
            "skill": skill,
            "title": result.get("title"),
            "url": result.get("link")
        })

    return results


print("🔎 Testing 'Machine Learning'")
courses = search_courses_via_serpapi("Machine Learning")
print("✅ Final course results:")
print(courses)