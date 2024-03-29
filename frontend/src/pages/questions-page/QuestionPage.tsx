import { useReducer, useRef, useState } from "react";
import { ProjectCreationQuestions } from "../../assets/TechStackQuestions";
import "./QuestionPage.css";

export type Question = {
    id: number;
    title: string;
    description: string;
    tags: string[];
    answers: Answer[];
};

type Answer = {
    id: number;
    description: string;
};

type QuestionPageProps = {
    nextPage: Function;
    addSavedAnswers: Function;
};

const QuestionPage = ({ nextPage, addSavedAnswers }: QuestionPageProps) => {
    // Will leave this for someone else, but set functions are not used, useEffect instead?
    const [questions, setQuestions] = useState<Question[]>(
        ProjectCreationQuestions
    );
    const [screenHeight, setScreenHeight] = useState<number>(
        window.innerHeight
    );

    const [currentQuestion, setCurrentQuestion] = useState<number>(0);
    const questionRef = questions.at(currentQuestion);
    const [selectedAnswers, setSelectedAnswers] = useState<Answer[]>([]);

    const handleAnswerClick = (answer: Answer) => {
        if (questionRef?.tags.includes("multiple"))
            setSelectedAnswers([...selectedAnswers, answer]);
        else setSelectedAnswers([answer]);
    };
    const handleNextClick = () => {
        const answerIds = selectedAnswers.map((answer) => `${answer.id}`);
        const tag = questionRef?.tags[0] ?? "other";
        addSavedAnswers(tag, answerIds);
        setSelectedAnswers([]);
        if (currentQuestion < questions.length - 1) {
            setCurrentQuestion(currentQuestion + 1);
        } else {
            nextPage("recommendation"); //savedAnswers);
        }
    };

    return (
        <div className="container">
            <div
                className="question-container"
                style={{ height: screenHeight / 1.5 }}>
                <QuestionCard
                    question={questionRef}
                    onAnswerClick={handleAnswerClick}
                    selectedAnswers={selectedAnswers}
                />
            </div>
            <div className="question-footer">
                <h3>
                    Question {currentQuestion + 1}/{questions.length}
                </h3>
                <button
                    className="button-81"
                    disabled={selectedAnswers.length === 0}
                    role="button"
                    onClick={handleNextClick}>
                    Next
                </button>
            </div>
        </div>
    );
};

const QuestionCard = ({ question, onAnswerClick, selectedAnswers }: any) => {
    return (
        <div className="question-card">
            <h1>{question.title}</h1>
            <div className="qustionTags">
                {question.tags.map((tag: string, i: number) => (
                    <span key={i} className="tags">
                        {tag}
                    </span>
                ))}
            </div>
            <br />
            <div className="answers">
                {question.answers.map((answer: Answer, i: number) => (
                    <div
                        key={i}
                        onClick={() => onAnswerClick(answer)}
                        className={`answer ${
                            selectedAnswers.includes(answer) && "selected"
                        }`}>
                        <h4>{answer.description}</h4>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default QuestionPage;
