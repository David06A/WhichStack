import json
import logging

import asyncio
import aiohttp

import motor.motor_asyncio as motor # Python driver for MongoDB #

# This will require the server edition of MongoDB #

import database

logging.basicConfig(level=logging.DEBUG)

class Handler:
    def __init__(self):
        self.database = database.Client() 

        self.stacks = {
            ""
        }

    async def retreive_response(self, prompt: str):
        async with aiohttp.ClientSession() as session:
            payload = {
                "prompt": "I want to make a mobile application"
            }
            url = 'https://localhost/ai_endpoint'

            async with session.get(url, json = payload) as response: 
                res = await response.json()
                logging.info(f"Received: {res}")
                return res

    async def get_stack_info(self, stack_type: int, stack_name: str):
        document = await self.database.load_document(stack_type, stack_name)

        stack_info = {
            "stack_type": document["stack_type"],
            "short_description": document["short_desc"],
            "long_description": document["long_desc"]
        }

    async def inc_suggested_counter(self, stack_type: int, stack_name: str):
        document = await self.database.load_document(stack_type, stack_name)

        # count += 1 #