import { useState } from "react";
import "../style/ResumeAnalyzer.css";
import "../style/share.css";
import { Link } from "react-router-dom";

const ResumeAnalyzer = () => {
  const [resume, setResume] = useState(null);
  const [keyword, setKeyword] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [activeTab, setActiveTab] = useState("job");
  const [progress, setProgress] = useState(0);
  const [status, setStatus] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!resume) return alert("Please upload a resume.");

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("keyword", keyword);

    setLoading(true);
    setProgress(0);
    setStatus("Starting...");

    const response = await fetch("http://localhost:5000/api/analyze-progress", {
      method: "POST",
      body: formData,
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");
    let buffer = "";

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      buffer += decoder.decode(value, { stream: true });
      const parts = buffer.split("\n\n");
      buffer = parts.pop(); // save incomplete chunk

      for (let part of parts) {
        if (part.startsWith("data: ")) {
          const jsonData = JSON.parse(part.replace("data: ", ""));
          if (jsonData.done) {
            setResult(jsonData.result);
            setLoading(false);
            setProgress(100);
            setStatus("Analysis complete!");
          } else if (jsonData.step) {
            setStatus(jsonData.step);
            setProgress((prev) => Math.min(prev + 10, 95));
          }
        }
      }
    }
  };

  return (
    <div className="analyzer-wrapper">
      <div className="nav-buttons fadeUp delay-1">
        <Link className="nav-button" to="/">Introduction</Link>
        <button className="nav-button active">Analysis</button>
      </div>

      <div className="analyzer-container fadeUp delay-2">
        <div className="analyzer-card">
          <form onSubmit={handleSubmit} className="form-area">
            <div className="upload-container">
              <label className="upload-btn">
                Upload Resume:
              </label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => setResume(e.target.files[0])}
                required
              />
            </div>

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

          {loading && (
            <>
              <p className="progress-status">{status}</p>
              <div className="progress-bar-container">
                <div className="progress-bar" style={{ width: `${progress}%` }}></div>
              </div>
            </>
          )}

          {result && (
            <>
              <div className="skills-box">
                <div className="skills-list">
                  <h3>Your skills:</h3>
                  {
                    result.resume_skills.map((skill, i) => (
                      <span key={i} className="skill-chip">{skill}</span>
                    ))
                  }
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
                {activeTab === "job" && result.jobs.map((job, i) => (
                  <div key={i} className="job-card">
                    <h4>{job.title} at {job.company}</h4>
                    <p className={`match-percent ${job.match_percent >= 80 ? "high" : job.match_percent >= 50 ? "medium" : "low"}`}>
                      Match: {job.match_percent.toFixed(1)}%
                    </p>
                    <p><strong>Matched:</strong> {job.matched_skills.join(", ")}</p>
                    <p><strong>Missing:</strong> {job.missing_skills.join(", ")}</p>
                    <a href={job.url} target="_blank" rel="noopener noreferrer">View Job</a>
                  </div>
                ))}

                {activeTab === "courses" && result.recommended_courses.map((rec, i) => (
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
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default ResumeAnalyzer;
