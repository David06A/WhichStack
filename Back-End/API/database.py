import json
import logging

import asyncio
import aiohttp

import motor.motor_asyncio as motor # Python driver for MongoDB #

# This will require the server edition of MongoDB #


logging.basicConfig(level=logging.DEBUG)

class Client:
    def __init__(self):
        self.database = motor.AsyncIOMotorClient('127.0.0.1', 27017) # Creates the Mongo client #
        logging.info(f"Created client:\n{self.database}")

    def setup_db(self): # Run this when creating the project #
        db = self.database["stack_db"]
        collection = db["full_stack"]

        setup_dict = {
            "_id": "react-native",
            "suggested_count": 0, # Number of times this stack has been output #
            "short_description": "React Native is a framework etcetc"
        }

        collection.insert_one(setup_dict)

    async def load_collection(self, stack_type: int): # Types 1-3 #
        db = self.database["stack_db"]

        match stack_type:
            case 1:
                collection = db["full_stack"]
            case 2:
                collection = db["front_end"]
            case 3:
                collection = db["back_end"]

        return collection

    async def load_document(self, stack_type: int, stack_name: str):
        collection = await self.load_collection(stack_type)
        document = await collection.find_one({"stack_name": stack_name}) # `Finds` the document using the stack name #

        return document
