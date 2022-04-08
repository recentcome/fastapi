from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app10 = APIRouter()

fake_db = {}


class Item(BaseModel):
    title: str
    timestramp: datetime
    desc: Optional[str] = None


@app10.put("/item/{id}")
def update_item(id: str, item: Item):
    json_item_data = jsonable_encoder(item)
    fake_db[id] = json_item_data
    return fake_db
