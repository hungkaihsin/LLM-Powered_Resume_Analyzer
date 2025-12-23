# JobFit AI

> An AI-powered web application that helps job seekers tailor their resumes by comparing them against real-time job postings and recommending upskilling courses.

##  Tech Stack
![Python](https://img.shields.io/badge/Python-3.x-blue)
![React](https://img.shields.io/badge/Frontend-React-61DAFB)
![Flask](https://img.shields.io/badge/Backend-Flask-000000)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-8E75B2)
![Cloud Run](https://img.shields.io/badge/Cloud-Google%20Cloud%20Run-4285F4)
![Firebase](https://img.shields.io/badge/Hosting-Firebase-FFCA28)

* **Languages:** Python, JavaScript, HTML, CSS
* **Frameworks/Libraries:** Flask, React, Vite, BeautifulSoup4, PyMuPDF
* **AI/ML:** Google Gemini API (Generative AI)
* **APIs:** Adzuna (Job Search), Serper (Course Search)
* **Infrastructure:** Google Cloud Run (Backend), Firebase Hosting (Frontend)

##  Key Features
* **Resume Parsing:** Extracts professional and technical skills from PDF resumes using AI.
* **Real-time Job Matching:** Scrapes live job postings and calculates a match percentage based on skill overlap.
* **Skill Gap Analysis:** Identifies missing skills required for specific job roles.
* **Smart Course Recommendations:** Automatically suggests relevant Coursera courses to bridge skill gaps.

##  Results / Demo
[Live Demo](https://resume-analyzer-482110.web.app)

* **Match Accuracy:** Uses fuzzy matching logic to compare resume skills against job descriptions with high precision.
* **Real-time Processing:** Streaming response implementation provides immediate feedback during the analysis pipeline.

##  How to Run

```bash
# Clone the repository
git clone https://github.com/hungkaihsin/NLP-LLM.git

# 1. Backend Setup
cd backend
pip install -r requirements.txt
# Create a .env file with GEMINI_API_KEY, ADZUNA_APP_ID, ADZUNA_API_KEY, SERPAPI_API_KEY
python src/app.py

# 2. Frontend Setup (in a new terminal)
cd frontend
npm install
npm run dev
```

##  Contact
Created by **Daniel** - [k_hung2@u.pacific.edu](mailto:k_hung2@u.pacific.edu) | [LinkedIn](https://www.linkedin.com/in/kai-hsin-hung/) | [Portfolio](https://hungkaihsin.github.io/)