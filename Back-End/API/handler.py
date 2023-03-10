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

    async def retreive_response(self, prompt: str):
        stacks = { # Test Data #
            "stacks": {
                "stack_one": {
                    "stack_type": 1,
                    "stack_name": "django"
                }
            }
        }
        
        return stacks

    async def get_stack_info(self, stack_type: int, stack_name: str):
        document = await self.database.load_document(stack_type, stack_name)
        logging.info(document, stack_type, stack_name)

        stack_info = {
            "stack_name": document["stack_name"],
            "short_description": document["short_description"],
            "long_description": document["long_description"]
        }

        return stack_info

    async def inc_suggested_counter(self, stack_type: int, stack_name: str):
        document = await self.database.load_document(stack_type, stack_name)

        # count += 1 #