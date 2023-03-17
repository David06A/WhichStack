import { useEffect, useState } from "react";
import { PopularStacks, Stack } from "../../assets/PopularStacks";
import "./HomePage.css";

type HomePageProps = {
    nextPage: Function;
};

export const HomePage = ( { nextPage }: HomePageProps ) =>
{
    const [ stacks, setStacks ] = useState<Stack[]>( PopularStacks );
    const [ screenHeight, setScreenHeight ] = useState<number>(
        window.innerHeight
    );

    return (
        <div className="container">
            <h1>Find your perfect tech stack in 60 seconds...</h1>
            <GoButton onClick={ nextPage } />
            <br />
            <hr />
            <h3>Popular Tech Stacks</h3>
            <div
                className="stack-container"
                style={ { height: screenHeight / 2 } }>
                { stacks.map( ( stack ) => (
                    <TechStackCard stack={ stack } />
                ) ) }
            </div>
        </div>
    );
};

const GoButton = ( { onClick }: any ) =>
{
    return (
        <button
            className="button-81"
            role="button"
            onClick={ () => onClick( "question" ) }>
            Get Started
        </button>
    );
};

type TechStackCardProps = {
    stack: Stack;
};

const TechStackCard = ( { stack }: TechStackCardProps ) =>
{
    return (
        <div className="techstack-card">
            <img className="stack-image" src={ stack.image } alt={ stack.name } />
            <h3 style={ { margin: 3 } }>{ stack.name }</h3>
            <p style={ { fontSize: 12 } }>{ stack.description }</p>
        </div>
    );
};
