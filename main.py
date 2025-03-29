from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()
@app.get("/headers")
async def get_headers(request: Request):
    user_agent = request.headers.get("User-Agent")
    accept_language = request.headers.get("Accept-Language")

    if not user_agent or not accept_language:
        return JSONResponse(status_code=400, content={"error": "Missing required headers"})

    # Необязательно: проверка формата Accept-Language
    if not validate_accept_language(accept_language): # type: ignore
        return JSONResponse(status_code=400, content={"error": "Invalid Accept-Language format"})

    return {
        "User-Agent": user_agent,
        "Accept-Language": accept_language
    }
import re

def validate_accept_language(language: str) -> bool:
    # Простая проверка формата, может быть расширена
    pattern = r"^([a-z]{2}-[A-Z]{2}|[a-z]{2})(,[a-z]{2};q=[0-9.]+)*$"
    return bool(re.match(pattern, language))
