from fastapi import Header, HTTPException
from .environment import configuration


async def get_token_header(x_token: str = Header(...)):
    if x_token != configuration["x-token"]:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return x_token
