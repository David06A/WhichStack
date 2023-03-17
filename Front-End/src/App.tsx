import { useState } from "react";
import reactLogo from "./assets/react.svg";
import "./App.css";
import { ThemeToggleButton } from "./components/ThemeToggleButton";
import { HomePage } from "./pages/home-page/HomePage";
import QuestionPage from "./pages/questions-page/QuestionPage";
import RecommendationPage from "./pages/recommendation/RecommendationPage";
function App() {
    const [isLightMode, setIsLightMode] = useState(false);
    const [currentPage, setCurrentPage] = useState("home");

    const updatePage = (page: string) => {
        setCurrentPage(page);
    };
    return (
        <div className="App" data-theme={!isLightMode ? "dark" : "light"}>
            <div>
                <div id="stars"></div>
                <div id="stars2"></div>
                <div id="stars3"></div>
                <div id="title"></div>
            </div>
            <div className="header">
                <div
                    className="align-row homebtn"
                    onClick={() => updatePage("home")}>
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
                <div
                    className={`page-container ${
                        currentPage !== "home" && "hidden"
                    }`}>
                    <HomePage nextPage={updatePage} />
                </div>
                <div
                    className={`page-container ${
                        currentPage !== "question" && "hidden"
                    }`}>
                    <QuestionPage nextPage={updatePage} />
                </div>
                <div
                    className={`page-container ${
                        currentPage !== "recommendation" && "hidden"
                    }`}>
                    <RecommendationPage />
                </div>
            </div>
        </div>
    );
}

export default App;
