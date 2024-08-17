// App.js

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import MainPage from "./MainPage";
import ChatbotPage from "./ChatbotPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/chatbot" element={<ChatbotPage />} />
        <Route path="/" element={<MainPage />} />
      </Routes>
    </Router>
  );
}

export default App;
