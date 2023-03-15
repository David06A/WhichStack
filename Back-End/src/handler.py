import json
import logging
import asyncio

import aiohttp
import motor.motor_asyncio as motor 

from database import Client
#from response import Response as ai


logging.basicConfig(level=logging.DEBUG)

class Handler:
    def __init__(self):
        self.database = Client() 
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
                "0": "I want to learn a new technology", 
                "1": "I want to build a portfolio piece",
                "2": "I want to build a product"
            },
            "budget": {
                "0": "I want to learn a new technology", 
                "1": "I want to build a portfolio piece",
                "2": "I want to build a product",
                "3": "I want to build a website"
            },
            "timeline": {
                "0": "I want to learn a new technology", 
                "1": "I want to build a portfolio piece",
                "2": "I want to build a product",
                "3": "I want to build a website"
            },
            "stacks": {
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
            "languages": {
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
            "database": {
                "0": "I want to learn a new technology", 
                "1": "I want to build a portfolio piece",
                "2": "I want to build a product",
                "3": "I want to build a website",
                "4": "I want to build a mobile app",
                "5": "I want to build a desktop app",
                "6": "I want to build a game"
            },
            "providers": {
                "0": "I want to learn a new technology", 
                "1": "I want to build a portfolio piece",
                "2": "I want to build a product",
                "3": "I want to build a website",
                "4": "I want to build a mobile app",
                "5": "I want to build a desktop app"
            }
        }

    async def retreive_response(self, ctx: dict):
        valid_ctx = await self.validate_context(ctx)
            
        if valid_ctx == False:
            return False

        e = "".join(f"{item}\n" for item in valid_ctx["purpose"].values())
        print(e)
        return "bob"

        #response_status, ai_response = await ai.request(formatted_ctx)

        #if not response_status:
            #return False

        #return ai_response

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
        print(ctx)

        for key in ctx:
            if key in self.valid_format and set(ctx[key]) <= set(self.valid_format[key]):
                for x in ctx[key]:
                    formatted_ctx[key][x] = self.valid_format[key][x]
            else:
                print(True, key)
                return False

        print(formatted_ctx)
        return formatted_ctx



    async def get_stack_info(self, stack_type: int, stack_name: str):
        document, _ = await self.database.load_document(stack_type, stack_name)

        stack_info = {
            "stack_name": document["stack_name"],
            "short_description": document["short_description"],
            "long_description": document["long_description"],
            "stack_count": document["stack_count"]
        }

        return stack_info

    async def inc_stack_count(self, stack_type: int, stack_name: str):
        document, collection = await self.database.load_document(stack_type, stack_name)

        await collection.update_one(
            {"stack_name": stack_name},
            {"$inc":
                {
                    "stack_count": 1
                }
            }
        )