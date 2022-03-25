# 请求体
from typing import Optional
from fastapi import APIRouter, Path, Body
from pydantic import BaseModel

app06 = APIRouter()


class Item(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app06.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int = Path(..., description='12'),
        q: Optional[str] = None,
        item: Optional[Item] = None):
    result = {"item_id": item_id}
    if q:
        result.update({"q": q})
    if item:
        result.update({"item": item})
    return result


class User(BaseModel):
    user_name: str
    user_id: int


@app06.put("/itemsup/{item_id}")
async def update_items(
        *,
        item_id: int = Path(..., description='123'),
        user: Optional[User] = None,
        # item: Optional[Item] = Body(..., embed=True),  # 单个Body参数的时候，可以使用embed参数。
        item: Optional[Item] = None,
        importance: int = Body(..., description='12344')  # 添加了body后，就不是查询参数，需要在body里面填写字段
):
    result = {"item_id": item_id, "importance": importance}
    if user:
        result.update({"user": user})
    if item:
        result.update({"item": item})
    return result
