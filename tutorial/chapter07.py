# 响应模型学习
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

app07 = APIRouter()


# response_model 使用该操作装饰器，可以自定义响应

class UserBase(BaseModel):
    user_name: str
    email: str


class UserOut(UserBase):
    pass


class UserIn(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str


@app07.put('/opt/', response_model=UserOut)
async def get_item(
        user: UserBase,
):
    return user


def hashed_password(password):
    return "secret" + password


def fake_save_user(user_in: UserIn):
    hashed_pw = hashed_password(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_pw)   # **user_in解包
    print("User saved!!!")
    return user_in_db


@app07.post("/usr/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_save = fake_save_user(user_in)
    return user_save


