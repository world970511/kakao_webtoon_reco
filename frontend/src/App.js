import React, { useState, useEffect } from "react";
import Preloader from "./components/Pre.jsx";
import Intro from "./components/Intro/Intro";
import Select from "./components/Select/Select";
import Result from "./components/Result/Result";
import Footer from "./components/Footer";
import {
  BrowserRouter as Router,
  Route,
  Routes
} from "react-router-dom";
import "./style.css";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";


function App() {
  const [load, upadateLoad] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => {
      upadateLoad(false);
    }, 1200);

    return () => clearTimeout(timer);
  }, []);

  return (
    <Router>
      <Preloader load={load} />
      <div className="App">
        <Routes>
          <Route path="/" element={<Intro />} />
          <Route path="/Select" element={<Select />} />
          <Route path="/Result" element={<Result />} />
        </Routes>
      </div>
      <Footer />
    </Router>
  );
}

export default App;

