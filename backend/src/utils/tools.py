import json
from src.config import ADZUNA_APP_ID, ADZUNA_API_KEY






# Save the results to jsonl file
def save_jsonl(filename, data_list):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data_list:
            f.write(json.dumps(item) + "\n")


