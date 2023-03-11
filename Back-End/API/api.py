# RESTful Request Library Of Choice #
from fastapi import FastAPI, Form, Request, Response, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# Ratelimit Handler For FastAPI #
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import uvicorn
import aiohttp

import json
import logging
import traceback
import asyncio
import traceback

from handler import Handler 


# Setup #
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(redoc_url=None, docs_url=None) #
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

logging.basicConfig(level=logging.DEBUG)

handler = Handler() # Utilities for the API #

#app.add_middleware(HTTPSRedirectMiddleware) # Optional/recommended SSL Cert #


@app.post("/stack/chooser")
#@limiter.limit("2/minute")
async def stack_chooser(request: Request, response: Response):
    try:
        req = await request.json()

        if not all(k in req for k in ("Q1","Q2")):
            return JSONResponse(
                content = {
                    "status_code": 400,
                    "error_message": "Bad Request",
                    "error_details": "The request body was missing required parameters"
                }
            )

        result = await handler.retreive_response("prompt_here")

        all_stacks = {} # All the stacks to be sent back to the client #    

        for stack in result["stacks"]: # In case there are multiple stacks #
            stack_type = result["stacks"][stack]["stack_type"]
            stack_name = result["stacks"][stack]["stack_name"]
            logging.info(result)

            stack_info = await handler.get_stack_info(stack_type, stack_name)
            all_stacks[stack_name] = stack_info 

            await handler.inc_stack_count(stack_type, stack_name)

        return_stacks = {
            "stacks": all_stacks
        }

        return JSONResponse(
            content = {
                "status_code": 200,
                "content" : return_stacks
            }
        )

    except Exception as error:
        if isinstance(error, json.decoder.JSONDecodeError):
            return JSONResponse(
                content = {
                    "status_code": 406,
                    "error_message": "Not Acceptable",
                    "error_details": "The request body was not a valid JSON string"
                }
            )
        else:
            logging.error(traceback.format_exc())
            return JSONResponse(
                content = {
                    "status_code": 500,
                    "error_message": "Internal Server Error"
                }
            )


if __name__ == '__main__':
    uvicorn.run(app, port=42069, host='0.0.0.0') # Hosts the API, binding to localhost # 