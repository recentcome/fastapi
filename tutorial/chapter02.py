from enum import Enum
from typing import Optional
from fastapi import APIRouter

app02 = APIRouter()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 查询参数学习
@app02.get("/items/")
async def read_item(skip: int, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# @app02.get('/items/{item_id}')
# async def read_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# 这里需要注意，如果接口都一样则优先请求写在前面的请求
# 可选参数+真假判断
# @app02.get('/items/{item_id}')
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if short:
#         item.update({"desc": "this is an amazing item"})
#     return item


# 必填参数
@app02.get('/items/{item_id}')
async def read_item(item_id: str, need: str):
    item = {"item_id": item_id}
    if need:
        item.update({"need": 1234})
    return item
