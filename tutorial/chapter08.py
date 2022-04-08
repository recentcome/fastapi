from fastapi import APIRouter, File, Form

from pydantic import BaseModel

app08 = APIRouter()


@app08.post("/files/")
async def create_file(
        files: bytes = File(...), token: str = Form(...)
):
    return {
        "file_size": len(files),
        "token": token
    }
