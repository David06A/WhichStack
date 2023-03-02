import { useState } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";
import { ThemeToggleButton } from "./components/ThemeToggleButton";
import { HomePage } from "./pages/home-page/HomePage";

function App() {
  const [count, setCount] = useState(0);
  const [isLightMode, setIsLightMode] = useState(false);

  return (
    <div className="App" data-theme={!isLightMode ? "dark" : "light"}>
      <div>
        <div id="stars"></div>
        <div id="stars2"></div>
        <div id="stars3"></div>
        <div id="title"></div>
      </div>
      <div className="header">
        <div className="align-row">
          <img src={reactLogo} className="logo" alt="logo" />
          <h1>WhichStack?</h1>
        </div>
        <div className="card">
          <ThemeToggleButton
            isLightMode={isLightMode}
            setIsLightMode={setIsLightMode}
          />
        </div>
      </div>
      <div className="card">
        {/*pages*/}
        <HomePage />
      </div>
    </div>
  );
}

export default App;
