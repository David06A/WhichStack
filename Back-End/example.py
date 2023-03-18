import asyncio
import json

import aiohttp

async def example():
    async with aiohttp.ClientSession() as session:
        payload = {
            "user_context": {
                "purpose": [
                    "2"
                ],
                "experience": [
                    "1"
                ],
                "budget": [
                    "1"
                ],
                "timeline": [
                    "1"
                ],
                "stacks": [
                    "4", "5"
                ],
                "languages": [
                    "4"
                ],
                "database": [
                    "4"
                ],
                "providers": [
                    "4"
                ]
            }
        }

        async with session.get('http://127.0.0.1:42069/stack/chooser', json = payload) as response:
            print(await response.json())

loop = asyncio.get_event_loop()
loop.run_until_complete(example())