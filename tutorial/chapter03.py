# 请求体
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    tax: Optional[float] = None


app03 = APIRouter()


@app03.post('/items')
async def create_item(item: Item):
    return item


@app03.post('/items{item_id}')
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app03.put('/items/{item_id}')
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
