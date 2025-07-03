import React from 'react';
import '../styles/Introduction.css';
import '../styles/shared.css';
import { Link } from 'react-router-dom';

const Introduction = () => {
  return (
    <div className="introduction-wrapper">
      <div className="nav-buttons fadeUp delay-1">
        <button className="nav-button active">Introduction</button>
        <Link className="nav-button" to="/analysis">Functionality</Link>
      </div>

      <div className="introduction-container fadeUp delay-2">
        <div className="introduction-card">
          <section>
            <h1>Welcome to Resume Analyzer</h1>
            <p>
              Bridge the gap between your resume and your dream job. This tool analyzes your resume against a job description, providing a match score and actionable insights to help you stand out.
            </p>
            <div className="cta-buttons">
              <Link className="cta-button" to="/analysis">Get Started</Link>
            </div>
          </section>

          <section>
            <h2>What it Does</h2>
            <p>
              Resume Analyzer is a powerful tool designed to help you tailor your resume for specific job opportunities. Here's how it works:
            </p>
            <ul>
              <li><strong>Resume Analysis:</strong> Upload your resume (PDF format), AI will extract your key skills.</li>
              <li><strong>Job Matching:</strong> Provide a job keyword, and the system will scrape relevant job postings.</li>
              <li><strong>Skill Comparison:</strong> Your resume skills are compared against the skills required for each job, generating a match percentage.</li>
              <li><strong>Identify Gaps:</strong> Discover which skills you're missing for your desired roles.</li>
              <li><strong>Course Recommendations:</strong> Get personalized recommendations for online courses to help you acquire the missing skills and boost your employability.</li>
            </ul>
          </section>



          <section>
            <h2>Contact Info</h2>
            <div className="contact-buttons">
              <a className="github" href="https://github.com/hungkaihsin" target="_blank" rel="noopener noreferrer">Github</a>
              <a className="linkedin" href="https://www.linkedin.com/in/kai-hsin-hung/" target="_blank" rel="noopener noreferrer">Linkedin</a>
              <a className="gmail" href="mailto:k_hung2@u.pacific.edu">Gmail</a>
            </div>
          </section>
        </div>

        </div>
      </div>
  );
};

export default Introduction;
