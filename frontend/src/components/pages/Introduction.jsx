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
            <h1>Welcome to Resume Optimizer AI</h1>
            <p>
              Bridge the gap between your resume and your dream job. This tool analyzes your resume against a job description, providing a match score and actionable insights to help you stand out.
            </p>
            <div className="cta-buttons">
              <Link className="cta-button" to="/analysis">Get Started</Link>
            </div>
          </section>

          <section>
            <h2>About the Creator</h2>
            <p>
              I'm a data science graduate student passionate about turning data into real-world impact. I have experience in machine learning (LSTM, ConvNets), backend API development, and SQL databases. Bilingual in Mandarin and English, I'm curious, collaborative, and driven to build smart, effective solutions.
            </p>
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
