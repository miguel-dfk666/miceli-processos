import { useEffect, useState } from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./home/homepage";
import CustomUserPage from "./auth/customuserpage";
import './styles/styles.css'
import LoginPage from "./auth/login";

function App() {
  const [processos, setProcessos] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}posts`);
        if (!response.ok) {
          throw new Error('Network response was not ok :(');
        }
        const result = await response.json();
        setProcessos(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }

    fetchData();
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/login" Component={LoginPage} />
        <Route path="/signup" Component={CustomUserPage} />
        <Route path="/" Component={() => <HomePage data={processos} />} />
      </Routes>
    </Router>
  );
}

export default App;
