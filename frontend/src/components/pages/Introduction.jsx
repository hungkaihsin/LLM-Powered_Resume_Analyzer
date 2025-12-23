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
            <h1>Welcome to JobFit AI</h1>
            <p>
              Bridge the gap between your resume and your dream job. JobFit AI analyzes your professional profile against real-time job market data, providing a match score and actionable insights to help you land the interview.
            </p>
            <div className="cta-buttons">
              <Link className="cta-button" to="/analysis">Start Analysis</Link>
            </div>
          </section>

          <section>
            <h2>How It Works</h2>
            <p>
              Our intelligent engine helps you tailor your resume for specific career paths in four simple steps:
            </p>
            <ul>
              <li><strong>Resume Parsing:</strong> Upload your PDF resume, and our AI instantly identifies your core professional and technical skills.</li>
              <li><strong>Real-Time Job Search:</strong> Enter a target role, and we'll scrape live job postings to understand current market demands.</li>
              <li><strong>Smart Matching:</strong> We compare your profile against actual job descriptions to calculate your fit percentage.</li>
              <li><strong>Upskilling Roadmap:</strong> Identify skill gaps and get direct links to relevant Coursera courses to close them.</li>
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