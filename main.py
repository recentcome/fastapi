import uvicorn
from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from tutorial import app01, app02, app03, app04, app05, app06, app07, app08, app09, app10
from tutorial.chapter09 import UnicornException

app = FastAPI()


@app.exception_handler(UnicornException)
async def unicore_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"messages": f"Oops {exc.name} dis somethiong"},
    )


app.include_router(app01, prefix="/chapter01", tags=['第一章 路径参数学习'])
app.include_router(app02, prefix="/chapter02", tags=['第二章 请求参数学习'])
app.include_router(app03, prefix="/chapter03", tags=['第三章 请求体学习'])
app.include_router(app04, prefix="/chapter04", tags=['第四章 查询参数和字符串校验学习'])
app.include_router(app05, prefix="/chapter05", tags=['第五章 路径参数和数值校验学习'])
app.include_router(app06, prefix="/chapter06", tags=['第六章 请求体-多个参数学习'])
app.include_router(app07, prefix="/chapter07", tags=['第七章 响应模型学习'])
app.include_router(app08, prefix="/chapter08", tags=['第八章 表单与文件学习'])
app.include_router(app09, prefix="/chapter09", tags=['第九章 错误处理学习'])
app.include_router(app10, prefix="/chapter10", tags=['第十章 json化数据'])



if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
