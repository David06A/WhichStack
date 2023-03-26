import React from "react";

function separateText(text: String) {
    if (!!!text || text === null) return { recommended: "", links: [] };

    const linkRegex = /https?:\/\/[^\s]+/g;
    const links = text.match(linkRegex);
    const textRegex = /(?:^|\s)(?!https?:\/\/)[^\s]+/g;
    const recommended = text.match(textRegex)?.join(" ").trim();
    return { recommended, links };
}

const formatText = (text: String) => {
    const sections = text.split(/(?:\r\n|\r|\n){2,}/g);

    return sections.map((section, index) => {
        const lines = section.split(/(?:\r\n|\r|\n)/g);
        const formattedLines = lines.map((line, i) => {
            if (
                line.match(
                    /(Frontend:|Backend:|Programming languages:|Database:|Hosting Provider:)/
                )
            ) {
                return <strong key={i}>{line}</strong>;
            }
            return <span key={i}>{line}</span>;
        });

        return (
            <p key={index}>
                {formattedLines.map((line, i) => (
                    <React.Fragment key={i}>
                        <div>{line}</div>
                        <br />
                    </React.Fragment>
                ))}
            </p>
        );
    });
};

type LinksProps = {
    links: string[];
};

const Links = ({ links }: LinksProps) => {
    return (
        <div>
            <div className="links">
                {links.map((link, index) => (
                    <a className="recommendation-text" key={index}>
                        {link}
                    </a>
                ))}
            </div>
        </div>
    );
};

export { formatText, separateText, Links };
