from src.job_title_generator import generate_titles_and_keywords_gemini
import google.generativeai as genai

if __name__ == "__main__":
    print("Using Gemini SDK from:", genai.__file__)
    print("Client class:", genai.GenerativeModel("models/gemini-pro")._client.__class__)
    result = generate_titles_and_keywords_gemini("Machine learning engineer in healthcare")
    print(result)