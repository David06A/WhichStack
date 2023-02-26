# RESTful Request Library Of Choice #
from fastapi import FastAPI, Form, Request, Response, Depends, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

# Ratelimit Handler For FastAPI #
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

import uvicorn

from handler import Handler 

import json
import traceback
import logging

import aiohttp
import asyncio


# Setup #
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(redoc_url=None, docs_url=None) #
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

logging.basicConfig(level=logging.DEBUG)

handler = Handler() # Utilities for the API #

#app.add_middleware(HTTPSRedirectMiddleware) # Optional/recommended SSL Cert #


@app.post("/query")
#@limiter.limit("2/minute")
async def query(request: Request, response: Response):
    try:
        logging.info(await request.json())
    except json.decoder.JSONDecodeError:
        logging.error("Request body could not be decoded")
        return "Error 400: Request Body Error"

    result = await handler.retreive_response("prompt_here")

    all_stacks = {} # All the stacks to be sent back to the client #    

    for stack in result["stacks"]: # In case there are multiple stacks #
        stack_type = result["stacks"][stack]["stack_type"]
        stack_name = result["stacks"][stack]["stack_name"]

        stack_info = await handler.get_stack_info(stack_type, stack_type)
        all_stacks[stack_name] = stack_info 

        await handler.inc_suggested_counter(stack_type, stack_name)

    return_json = {
        "stacks": all_stacks
    }

    return JSONResponse(status_code = 200, content=return_json, media_type="application/json")


if __name__ == '__main__':
    uvicorn.run(app, port=9000, host='0.0.0.0') # Hosts the API, binding to localhost # 