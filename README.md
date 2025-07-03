# Resume Analyzer with AI-Powered Skill Matching and Course Recommendations (Local Demo)

This is a local-only demonstration of a full-stack web application designed to analyze resumes, extract key skills, compare them against job descriptions, and suggest relevant online courses. This version is configured to run entirely offline, using mock data and simplified logic to replace external API calls, making it easy to set up and showcase.

## Features

*   **Resume Analysis:** Upload a PDF resume to extract skills.
*   **Job Matching:** Compare extracted resume skills against a job keyword to see skill matches and gaps.
*   **Course Recommendations:** Get suggestions for online courses based on identified missing skills.
*   **Local-First:** All core functionalities run without external API keys or internet access (after initial setup).

## Technologies Used

*   **Frontend:** React (Vite), HTML, CSS
*   **Backend:** Python (Flask)
*   **PDF Parsing:** `pdfminer.six`
*   **Skill Comparison:** `fuzzywuzzy`

## Setup Instructions

Follow these steps to get the application running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Backend Setup

Navigate to the `backend` directory, create a virtual environment, and install dependencies:

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Frontend Setup

Open a new terminal tab/window, navigate to the `frontend` directory, and install Node.js dependencies:

```bash
cd ../frontend
npm install
```

## Running the Application

### 1. Start the Backend Server

In your backend terminal (where you activated the virtual environment):

```bash
python src/app.py
```

The backend server should start on `http://127.0.0.1:5001/`.

### 2. Start the Frontend Development Server

In your frontend terminal:

```bash
npm run dev
```

The frontend development server will start, typically on `http://localhost:5173/`.

### 3. Access the Application

Open your web browser and navigate to the URL provided by the `npm run dev` command (e.g., `http://localhost:5173/`).

## Important Notes

*   **API-Free Operation:** This version uses mock data and simplified logic for job scraping, skill extraction, and course recommendations. It does not make calls to external APIs (Google Gemini, Adzuna, Serper).
*   **Original Version:** The original, API-driven version of this project is deployed on Render. If you wish to see the full functionality with real API integrations, please refer to the live demo (link to your Render deployment).

## Contributing

Feel free to fork this repository and contribute!

## License

[Specify your license here, e.g., MIT License]