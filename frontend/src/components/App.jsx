// src/App.jsx
import { HashRouter, Routes, Route, Navigate } from 'react-router-dom'
import ResumeAnalyzer from './pages/ResumeAnalyzer.jsx'
import Introduction from './pages/Introduction.jsx';
import './App.css'
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <HashRouter>
    <Toaster position="top-right" reverseOrder={false} />
      <Routes>
        <Route path="/" element={<Navigate to="/intro" replace />} />
        <Route path="/analysis" element={<ResumeAnalyzer />} />
        <Route path="/intro" element={<Introduction />} />
        {/* later you can add more pages here */}
      </Routes>
    </HashRouter>
  )
}

export default App