import uvicorn
from fastapi import FastAPI

from tutorial import app01, app02, app03, app04, app05, app06

app = FastAPI()
app.include_router(app01, prefix="/chapter01", tags=['第一章 路径参数学习'])
app.include_router(app02, prefix="/chapter02", tags=['第二章 请求参数学习'])
app.include_router(app03, prefix="/chapter03", tags=['第三章 请求体学习'])
app.include_router(app04, prefix="/chapter04", tags=['第四章 查询参数和字符串校验学习'])
app.include_router(app05, prefix="/chapter05", tags=['第五章 路径参数和数值校验学习'])
app.include_router(app06, prefix="/chapter06", tags=['第六章 请求体-多个参数学习'])
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)