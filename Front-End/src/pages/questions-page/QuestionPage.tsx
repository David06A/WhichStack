import { useState } from "react";
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
};

const QuestionPage = ({ nextPage }: any) => {
    const [questions, setQuestions] = useState<Question[]>(
        ProjectCreationQuestions
    );

    const savedAnswers = [];
    const [currentQuestion, setCurrentQuestion] = useState<number>(0);
    const questionRef = questions.at(currentQuestion);
    const [selectedAnswers, setSelectedAnswers] = useState<Answer[]>([]);

    const handleAnswerClick = (answer: Answer) => {
        if (questionRef?.tags.includes("multiple"))
            setSelectedAnswers([...selectedAnswers, answer]);
        else setSelectedAnswers([answer]);
    };
    const handleNextClick = () => {
        savedAnswers.push(selectedAnswers);
        setSelectedAnswers([]);
        if (currentQuestion < questions.length - 1) {
            setCurrentQuestion(currentQuestion + 1);
        } else {
            nextPage("techStackPage"); //savedAnswers);
        }
    };

    return (
        <div className="container">
            <h1>Question Page</h1>
            <br />
            <hr />
            <div className="question-container">
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
            <h2>{question.title}</h2>
            <div className="qustionTags">
                {question.tags.map((tag: string) => (
                    <span className="tags">{tag}</span>
                ))}
            </div>
            <br />
            <div className="answers">
                {question.answers.map((answer: Answer) => (
                    <div
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
