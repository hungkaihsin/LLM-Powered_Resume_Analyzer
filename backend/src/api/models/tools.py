import json
from dotenv import load_dotenv
import os
load_dotenv()

# variables in .env file

# Gemini
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Adzuna
ADZUNA_APP_ID = os.getenv('ADZUNA_APP_ID')
ADZUNA_API_KEY = os.getenv('ADZUNA_API_KEY')






# Save the results to jsonl file
def save_jsonl(filename, data_list):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data_list:
            f.write(json.dumps(item) + "\n")


