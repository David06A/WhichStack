import json
import logging
import asyncio

import aiohttp
import motor.motor_asyncio as motor

from response import Response as ai


logging.basicConfig(level=logging.INFO)


class Handler:
    def __init__(self):
        self.valid_format = {
            "purpose": {
                "0": "I want to learn a new technology",
                "1": "I want to build a portfolio piece",
                "2": "I want to build a product",
                "3": "I want to build a website",
                "4": "I want to build a mobile app",
                "5": "I want to build a desktop app",
                "6": "I want to build a game",
                "7": "I want to build a chat bot",
                "8": "I want to build a web scraper"
            },
            "experience": {
                "0": "I am a begineer",
                "1": "I am an intermediate developer",
                "2": "I am an advanced developer"
            },
            "budget": {
                "0": "I have no budget/no funds",
                "1": "I have a small budget",
                "2": "I have a medium budget",
                "3": "I have a large budget"
            },
            "timeline": {
                "0": "I have no timeframe",
                "1": "I have a short timeframe",
                "2": "I have a medium timeframe",
                "3": "I have a long timeframe"
            },
            "stacks": {
                "0": "I have no preference",
                "1": "I want to use React",
                "2": "I want to use Angular",
                "3": "I want to use Vue",
                "4": "I want to use Node",
                "5": "I want to use GraphQL",
                "6": "I want to use AWS",
                "7": "I want to use Azure",
                "8": "I want to use Docker"
            },
            "languages": {
                "0": "I have no preference",
                "1": "I want to use JavaScript",
                "2": "I want to use TypeScript",
                "3": "I want to use Python",
                "4": "I want to use Java",
                "5": "I want to use C#",
                "6": "I want to use C++",
                "7": "I want to use Go",
                "8": "I want to use Rust"
            },
            "database": {
                "0": "I have no preference",
                "1": "I want to use MongoDB",
                "2": "I want to use MySQL",
                "3": "I want to use PostgreSQL",
                "4": "I want to use DynamoDB",
                "5": "I want to use Redis",
                "6": "I want to use Cassandra"
            },
            "providers": {
                "0": "I have no preference",
                "1": "I want to use AWS",
                "2": "I want to use GCP",
                "3": "I want to use Azure",
                "4": "I want to use Digital Ocean",
                "5": "I want to use Heroku",
            }
        }

    async def retreive_response(self, ctx: dict):
        logging.info("Requesting response")
        ai_response = await ai().request(ctx)

        if not ai_response:
            return False

        return ai_response

    async def validate_context(self, ctx: dict):
        formatted_ctx = {
            "purpose": {},
            "experience": {},
            "budget": {},
            "timeline": {},
            "stacks": {},
            "languages": {},
            "database": {},
            "providers": {}
        }

        for key in ctx:
            if key in self.valid_format and set(ctx[key]) <= set(self.valid_format[key]):
                for x in ctx[key]:
                    formatted_ctx[key][x] = self.valid_format[key][x]
            else:
                return False

        return formatted_ctx
