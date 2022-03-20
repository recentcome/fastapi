import uvicorn
from fastapi import FastAPI

from tutorial import app01

app = FastAPI()
app.include_router(app01, prefix="/chapter01", tags=['nihao'])
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)