# 路径参数和数值校验

from pydantic import BaseModel
from fastapi import APIRouter, Query, Path
from typing import Optional, List

app05 = APIRouter()


@app05.get('/item/{item_id}')
async def get_item(q: str = "", item_id: int = Path(..., description='这是一个路径参数')):
    result = {'itemId': item_id}
    if q:
        result.update({"q": q})
    return result


@app05.get('/items/{item_id}')
async def get_items(*, q: str, item_id: int = Path(..., description='123')):
    result = {"item_id", item_id}
    if q:
        result.update({"q": q})
    return result
