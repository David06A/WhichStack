from fastapi import FastAPI, Request, Response, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

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


limiter = Limiter(key_func=get_remote_address)
app = FastAPI(redoc_url=None, docs_url=None)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

#app.add_middleware(HTTPSRedirectMiddleware)

logging.basicConfig(level=logging.INFO)

handler = Handler()

@app.get("/stack/chooser")
@limiter.limit("10/hour")
async def stack_chooser(request: Request, response: Response):
    try:
        req = await request.json()

        if not isinstance(req, dict):
            return JSONResponse(
                content = {
                    "status": 406,
                    "error" : "The request body was not a valid JSON string"
                }
            )

        valid_ctx = await handler.validate_context(req["user_context"])
            
        if valid_ctx is False:
            return JSONResponse(
                content = {
                    "status": 400,
                    "error" : "The request body is missing required elements"
                }
            )

        result = await handler.retreive_response(valid_ctx)

        if result is None:
            return HTTPException(status_code=500, detail="The server is unable to handle your request at this time")

        return JSONResponse(
            content = {
                "status": 200,
                "type": "success",
                "response" : result["choices"][0]["message"]["content"]
            }
        )

    except Exception as error:
        logging.error(traceback.format_exc())
        return HTTPException(status_code=500, detail="The server is unable to handle your request at this time")


if __name__ == '__main__':
    uvicorn.run(app, port=42069, host='0.0.0.0')