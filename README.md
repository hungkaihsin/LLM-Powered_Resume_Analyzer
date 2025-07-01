# Resume Optimizer AI

[Link to the website](https://your-deployment-link.com)

Resume Optimizer AI is a web application designed to help job seekers tailor their resumes to specific job descriptions. By leveraging Natural Language Processing (NLP) and Large Language Models (LLMs), this tool analyzes your resume, compares it against a target job posting, and provides a match percentage. It also identifies skill gaps and recommends relevant online courses to enhance your qualifications.

## About The Project

This project demonstrates the ability to integrate and manage NLP and LLM technologies in a practical application. It provides users with actionable insights to improve their resumes and increase their chances of landing an interview. The backend is powered by Python, and the frontend is built with React.

## Key Features

- **Resume Analysis:** Upload your resume (PDF or DOCX) to have it parsed and analyzed.
- **Skill Extraction:** Utilizes Google's Gemini API to intelligently extract skills, experience, and education from your resume.
- **Job Scraping:** Scrapes job postings from popular platforms to get real-time job requirements.
- **Match Percentage:** Calculates and displays a percentage score indicating how well your resume matches a target job description.
- **Course Recommendations:** Recommends online courses from various platforms to help you fill any identified skill gaps.

## Tech Stack

- **Frontend:** React, Vite, CSS
- **Backend:** Python, Flask/FastAPI (or similar)
- **AI/ML:** Google Gemini API
- **Libraries:** Beautiful Soup (for scraping), PyMuPDF (for PDF processing)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Node.js and npm
- Python 3.x

### Installation

1.  **Clone the repo**
    ```sh
    git clone https://github.com/your_username/NLP-LLM.git
    ```
2.  **Install NPM packages for the frontend**
    ```sh
    cd frontend
    npm install
    ```
3.  **Install Python packages for the backend**
    ```sh
    cd ../backend
    pip install -r requirements.txt
    ```

### Usage

1.  **Start the backend server**
    ```sh
    cd backend/src
    python app.py
    ```
2.  **Start the frontend development server**
    ```sh
    cd ../../frontend
    npm run dev
    ```
3.  Open your browser and navigate to `http://localhost:5173` (or the address shown in your terminal).

## Contact

Daniel - [k_hung2@u.pacific.edu](mailto:k_hung2@u.pacific.edu)

Project Link: [https://github.com/hungkaihsin/NLP-LLM](https://github.com/hungkaihsin/NLP-LLM)
