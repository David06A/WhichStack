import React, { useState } from "react";
import "./Recommendation.css";

// handle data from backend
const RecommendationPage = () =>
{
    const [ screenHeight, setScreenHeight ] = useState<number>(
        window.innerHeight
    );

    return (
        <div className="container" style={ { height: screenHeight / 1.5 } }>
            <div className="recomendation">
                <div className="recom-container">
                    <h1>We recommend the following</h1>

                    <Recommendation />
                </div>
                <div>
                    <p className="recommendation-text">
                        Find affiliate Links for the recommended stack below
                    </p>
                    <Links />
                </div>
            </div>
        </div>
    );
};

// the text variable will take in the output from the backend
const text =
    "Based on your advanced experience in programming, desired tech stacks and budget, I recommend using the following tech stack to build your website:Front-end:- React - A popular and widely used front-end framework that allows you to build interactive user interfaces easily. Its virtual DOM feature helps in improving the website's performance.- Vue - A lightweight, easy-to-learn front-end framework that excels in building single-page applications quickly.Back-end:- Node.js - A JavaScript runtime that allows you to write server-side code with ease. Since you're familiar with JavaScript, it should be easy to pick up. It also has an extensive collection of open-source packages available to use.Programming languages:- Java - A popular programming language that allows you to build reliable, high-performance applications. It is user-friendly and has a large community for support.Database:- MongoDB - A document-based database that is very suitable for storing large amounts of data. Its flexible schema allows you to store data of varying structures.Hosting providers:- Heroku - Offers a free tier that allows you to deploy your website with ease. It has excellent documentation, and it's well optimized for hosting websites.I believe this tech stack is good because:- React and Vue can easily integrate with Node.js for server-side rendering, allowing for better user experience and improved SEO.- Java can be easily integrated with Node.js, allowing the back-end and front-end to communicate with ease.- MongoDB can be deployed easily on Heroku.References:- React - https://reactjs.org/- Vue - https://vuejs.org/- Node.js - https://nodejs.org/en/- Java - https://www.java.com/en/- MongoDB - https://www.mongodb.com/- Heroku - https://www.heroku.com/";
var recommendedText = "";
var linkText = "";

// this regex function will split the text when it sees References:
function separateText ( text: any )
{
    const regex = /^(.*?)(?=\bReferences:)/is;
    const [ , recommended ] = regex.exec( text );
    const links = text.replace( recommended, "" );
    recommendedText = recommended;
    linkText = links;
    console.log( recommendedText, linkText );
}

separateText( text );

const Recommendation = () =>
{
    return (
        <div style={ { padding: 5 } }>
            <p>{ recommendedText }</p>
        </div>
    );
};

const Links = () =>
{
    return (
        <div>
            <div className="links">
                { linkText.split( "-" ).map( ( line, index ) => (
                    <p className="recommendation-text" key={ index }>
                        { line }
                    </p>
                ) ) }
            </div>
        </div>
    );
};

export default RecommendationPage;
