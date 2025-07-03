import { useState } from "react";
import "../styles/ResumeAnalyzer.css";
import "../styles/shared.css";
import { Link } from "react-router-dom";
import { toast } from "react-hot-toast";
const BASE_URL = 'http://localhost:5001';

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
    if (!resume) {
    toast.error("Please upload a resume file.");
    return;
    }
    if (!keyword.trim()) {
      toast.error("Please enter a job keyword.");
      return;
    }


    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("keyword", keyword);

    setLoading(true);
    setProgress(0);
    setStatus("Starting...");

    const response = await fetch(`${BASE_URL}/api/analyze-progress`, {
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
        <button className="nav-button active">Functionality</button>
      </div>

      <div className="analyzer-container fadeUp delay-2">
        <div className="analyzer-card">
          <form onSubmit={handleSubmit} className="form-area">
            <div className="upload-container">
              <label className="upload-btn">
                Upload Resume (.pdf):
              </label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => {
                  const file = e.target.files[0];
                  if (file) {
                    setResume(file);
                    toast.success("Resume uploaded successfully!");
                  }
                }}
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
            <button
              type="submit"
              className="submit-btn"
              disabled={loading}
            >

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

              <div className={`results-box fade ${result ? "fadeUp delay-1" : ""}`} key={activeTab}>
                {activeTab === "job" && result?.jobs.map((job, i) => (
                  <div key={i} className="job-card">
                    <h4>{job.title} at {job.company}</h4>
                    <p className={`match-percent ${job.match_percent >= 80 ? "high" : job.match_percent >= 50 ? "medium" : "low"}`}>
                      Match: {job.match_percent.toFixed(1)}%
                    </p>
                    <p><strong>Matched:</strong> {job.matched_skills.join(", ")}</p>
                    <p><strong>Missing:</strong> {job.missing_skills.join(", ")}</p>
                    <div className="job-link-container">
                    <a href={job.url} target="_blank" rel="noopener noreferrer">View Job</a>
                    </div>
                  </div>
                ))}

                  {activeTab === "courses" && result?.recommended_courses.map((rec, i) => (
                    <div key={i} className="course-block">
                      <h4 className="course-skill">{rec.skill}</h4>
                      <ul className="course-list">
                        <h3>Links to courses:</h3>
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
