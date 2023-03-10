import { useState } from "react";
import { PopularStacks, Stack } from "../../assets/PopularStacks";
import "./HomePage.css";

type HomePageProps = {};

export const HomePage = ({}: HomePageProps) => {
    const [stacks, setStacks] = useState<Stack[]>(PopularStacks);
    return (
        <div className="container">
            <h1>Find your perfect tech stack in 60 seconds...</h1>
            <GoButton />
            <br />
            <hr />
            <h3>Popular Tech Stacks</h3>
            <div className="stack-container">
                {stacks.map((stack) => (
                    <TechStackCard stack={stack} />
                ))}
            </div>
        </div>
    );
};

const GoButton = () => {
    return (
        <button className="button-81" role="button">
            Get Started
        </button>
    );
};

type TechStackCardProps = {
    stack: Stack;
};
const TechStackCard = ({ stack }: TechStackCardProps) => {
    return (
        <div className="techstack-card">
            <img className="stack-image" src={stack.image} alt={stack.name} />
            <h3 style={{ margin: 3 }}>{stack.name}</h3>
            <p style={{ fontSize: 12 }}>{stack.description}</p>
        </div>
    );
};
