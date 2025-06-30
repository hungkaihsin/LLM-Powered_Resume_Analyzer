import { useState } from "react";
import axios from "axios";
import "./ResumeAnalyzer.css"; // custom CSS

const ResumeAnalyzer = () => {
  const [resume, setResume] = useState(null);
  const [keyword, setKeyword] = useState("machine learning");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState("job");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!resume) return alert("Please upload a resume.");

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("keyword", keyword);

    setLoading(true);
    try {
      const res = await axios.post("http://localhost:5000/api/analyze", formData);
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Failed to analyze resume.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <nav className="nav-bar">
        <button className="nav-btn">Introduction</button>
        <button className="nav-btn active">Analysis</button>
      </nav>

      <div className="inner-box">
        <form onSubmit={handleSubmit} className="form-area">
          <label className="upload-btn">
            Upload Resume:
            <input type="file" accept=".pdf" onChange={(e) => setResume(e.target.files[0])} required />
          </label>

          <input
            className="keyword-input"
            type="text"
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
            placeholder="Enter job keyword"
          />
          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? "Analyzing..." : "Submit"}
          </button>
        </form>

        <div className="skills-box">
          <h3>Your skills:</h3>
          <div className="skills-list">
            {result?.resume_skills.map((skill, i) => (
              <span key={i} className="skill-chip">{skill}</span>
            ))}
          </div>
        </div>

        <div className="tab-controls">
          <button
            className={`tab-btn ${activeTab === "job" ? "active-tab" : ""}`}
            onClick={() => setActiveTab("job")}
          >
            Job match
          </button>
          <button
            className={`tab-btn ${activeTab === "courses" ? "active-tab" : ""}`}
            onClick={() => setActiveTab("courses")}
          >
            Online courses
          </button>
        </div>

        <div className="results-box">
          {activeTab === "job" && result?.jobs.map((job, i) => (
            <div key={i} className="job-card">
              <h4>{job.title} at {job.company}</h4>
              <p>Match: {job.match_percent}%</p>
              <p><strong>Matched:</strong> {job.matched_skills.join(", ")}</p>
              <p><strong>Missing:</strong> {job.missing_skills.join(", ")}</p>
              <a href={job.url} target="_blank" rel="noopener noreferrer">View Job</a>
            </div>
          ))}

          {activeTab === "courses" && result?.recommended_courses.map((rec, i) => (
            <div key={i}>
              <h4>{rec.skill}</h4>
              <ul>
                {rec.courses.map((c, idx) => (
                  <li key={idx}>
                    <a href={c.url} target="_blank" rel="noopener noreferrer">
                      {c.title}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div className="page-footer">Page #</div>
      </div>
    </div>
  );
};

export default ResumeAnalyzer;
