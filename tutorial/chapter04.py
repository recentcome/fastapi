# 查询参数和字符串校验

from pydantic import BaseModel
from fastapi import APIRouter, Query
from typing import Optional, List

app04 = APIRouter()


@app04.get('/item/')
async def read_items(q: Optional[str] = Query(None, max_length=20)):
    if q:
        return {"q": q}
    else:
        return {"message": "your item is not none"}


@app04.get('/item1/')
async def read_items1(q: str = Query(..., max_length=20)):
    if q:
        return {"q": q}
    else:
        return {"message": "your item is not none"}


# 查询参数列表/多个值
@app04.get('/item1list/')
async def read_items_list(q: Optional[List[str]] = Query(..., max_length=20, description="123")):
    if q:
        return {"q": q}
