import google.generativeai as genai
from src.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_titles_and_keywords_gemini(career_goal: str):
    model = genai.GenerativeModel("gemini-flash-latest")  
    prompt = f"""
    Based on the user's goal: "{career_goal}", 
    generate:
    - 5 related job titles
    - 10 search keywords

    Return in JSON format:
    {{
        "titles": [...],
        "keywords": [...]
    }}
    """
    response = model.generate_content(prompt)
    return response.text