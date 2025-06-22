from src.job_title_generator import generate_titles_and_keywords_gemini

if __name__ == "__main__":
    result = generate_titles_and_keywords_gemini("Machine learning engineer in healthcare")
    print(result)