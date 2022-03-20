from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CityInfo(BaseModel):
    province: str
    country: str
    is_affected: Optional[bool] = None


@app.get('/')
async def hello():
    return {"hello": "world"}


@app.get('/city/{city}')
async def hello(city: str, query: Optional[str] = None):
    return {"hello": city}


@app.put('/city/{city}')
async def hello(city: str, city_info: CityInfo):
    return {"city": city, "provice": city_info.province, "country": city_info.country, "is_affected": city_info.is_affected}

if __name__ == '__main__':
    uvicorn.run("hello_world:app", reload=True)