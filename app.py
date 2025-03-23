from fastapi import FastAPI

from fastapi import HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def home():
    return Response(content="Welcome to the GitHUB Actions workflow", media_type="text/plain")