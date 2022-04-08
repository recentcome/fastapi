# 请求体
from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Path, Body
from pydantic import BaseModel, Field

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


class ItemNew(BaseModel):
    name: str
    desc: Optional[str] = Field(None, title='nihao etem', max_length=20)
    price: float = Field(..., gt=0, description='nihaoya')
    tax: Optional[float] = None

    class Config:
        dgsdg = {
            "23454": {
                "name": "Foo",
                "desc": "a very nice item",
                "price": 35.24,
                "tax": 23.4,
            }
        }


@app06.put("/items_field/{item_id}")
async def update_field_items(
        item_id: int,
        # item: ItemNew = Body(..., embed= Ture)   # 添加了body后，就不是查询参数，需要在body里面填写字段,使用embed参数后，格式如下：
        # {
        #   "item":
        #   {
        #   "name": "",
        #   "desc": "",
        #   "price": "",
        #   "tax": ""
        #   }
        # }
        # 增加了key字段
        item: Optional[ItemNew] = None
):
    results = {"items_id": item_id, "item": item}
    return results


@app06.put('/items_op/{items_id}')
async def read_items(
        item_id: UUID,
        start_time: Optional[datetime] = Body(None),
        end_time:Optional[datetime] = Body(None),
        repeat_at: Optional[time] = Body(None),
        process_after: Optional[timedelta] = Body(None),
):
    start_process = start_time + process_after
    duration = end_time - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_time,
        "end_datetime": end_time,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


