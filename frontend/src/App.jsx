// src/App.jsx
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import ResumeAnalyzer from './pages/ResumeAnalyzer.jsx'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/analysis" replace />} />
        <Route path="/analysis" element={<ResumeAnalyzer />} />
        {/* later you can add more pages here */}
      </Routes>
    </BrowserRouter>
  )
}

export default App