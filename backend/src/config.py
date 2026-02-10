import os
from dotenv import load_dotenv
load_dotenv()

# Use .strip() to remove any accidental newlines or spaces from the keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID", "").strip()
ADZUNA_API_KEY = os.getenv("ADZUNA_API_KEY", "").strip()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "").strip()
PORT = os.getenv('PORT')

print(f"DEBUG: GEMINI_API_KEY set: {bool(GEMINI_API_KEY)}")
print(f"DEBUG: ADZUNA_APP_ID set: {bool(ADZUNA_APP_ID)}")
print(f"DEBUG: SERPAPI_API_KEY set: {bool(SERPAPI_API_KEY)}")