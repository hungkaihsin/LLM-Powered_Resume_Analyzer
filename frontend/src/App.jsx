// src/App.jsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import ResumeAnalyzer from './pages/ResumeAnalyzer.jsx'
import './App.css'
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <BrowserRouter>
    <Toaster position="top-right" reverseOrder={false} />
      <Routes>
        <Route path="/" element={<Navigate to="/analysis" replace />} />
        <Route path="/analysis" element={<ResumeAnalyzer />} />
        {/* later you can add more pages here */}
      </Routes>
    </BrowserRouter>
  )
}

export default App