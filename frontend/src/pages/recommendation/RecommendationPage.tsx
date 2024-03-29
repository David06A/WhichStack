import React, { useEffect, useRef, useState } from "react";
import { examplePayload } from "../../assets/ExamplePayload";
import { formatText, Links, separateText } from "./helpers/FormatText";
import "./Recommendation.css";

type RecommendationPageProps = {
    savedAnswers: Object;
};

const RecommendationPage = ({ savedAnswers }: RecommendationPageProps) => {
    const [screenHeight, setScreenHeight] = useState<number>(
        window.innerHeight
    );

    const isRequesting = useRef<boolean>(false);
    const [chatGPT, setChatGPT] = useState<undefined | string>(undefined);
    const payload = { user_context: { ...savedAnswers } };
    console.log(payload, examplePayload);
    useEffect(() => {
        if (isRequesting.current) return;
        isRequesting.current = true;
        fetch("http://127.0.0.1:42069/stack/chooser", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                setChatGPT(data.response);
            })
            .finally(() => {
                isRequesting.current = false;
            });
    }, []);

    console.log(chatGPT);
    if (chatGPT === undefined || isRequesting.current)
        return <div className="spinner"></div>;

    const recommendedText = separateText(chatGPT);

    return (
        <div className="container" style={{ height: screenHeight / 1.25 }}>
            <div className="recomendation">
                <div className="recom-container">
                    <div>{formatText(recommendedText.recommended ?? "")}</div>
                    <h3>
                        Find affiliate Links for the recommended stack below
                    </h3>
                    <br />
                    <Links links={recommendedText.links ?? []} />
                </div>
            </div>
        </div>
    );
};

export default RecommendationPage;
