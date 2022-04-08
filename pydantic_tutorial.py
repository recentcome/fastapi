from datetime import datetime, date, time
from typing import List, Optional
from pathlib import Path

from pydantic import BaseModel, ValidationError
from pydantic.types import constr
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel):
    id: int
    name: str = "nih"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


print("\033[31m1. --- Basemodel ---\033[0m")

external_data = {
    "id": "123",
    "signup_ts": "2022-3-20 11:21",
    "friends": [1, 2, "3"]
}
# python解包，两个*只能对字典对象进行解包
user = User(**external_data)
print(user.dict())

print("\033[31m2. --- 校验失败处理 ---\033[0m")

try:
    User(id=1, signup_ts=datetime.today(), friends=[1, 2, "no int"])
except ValidationError as e:
    print(e.json())

print("\033[31m3. --- 模型类的属性和方法 ---\033[0m")
print(user.dict())
print(user.json())
print(user.copy())  # 浅拷贝

# 解析数据
print(User.parse_obj(obj=external_data))
# 解析key value值
print(User.parse_raw('{"id": "123","signup_ts": "2022-3-20 11:21","friends": [1, 2, "3"]}'))

path = Path("./pydantic.json")
path.write_text('{"id": "123","signup_ts": "2022-3-20 11:21","friends": [1, 2, "3"]}')
# 解析文件
print(User.parse_file(path))

# 数据格式
print(user.schema())
print(user.schema_json())

# print(user.construct)
print(User.__fields__.keys())  # 定义模型类时，所有的类型都注明，顺序就不会乱

print("\033[31m3. --- 递归模型 ---\033[0m")


class Sound(BaseModel):
    sound: str


class Dog(BaseModel):
    birthday: date
    weight: float = Optional[None]
    sound: List[Sound]


dog = Dog(birthday=date.today(), weight=6.6, sound=[{"sound": "wangwwang"}, {"sound": "yingying"}])
print(dog.dict())

print("\033[31m3. --- ORM模型 ---\033[0m")

Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), nullable=False)
    name = Column(String(20), unique=True, nullable=False)
    domains = Column(ARRAY(String(20)))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=20)
    domains: List

    class Config:
        orm_mode = True


co_orm = Company(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['www.baidu.com', 'www.sohu.com']
)

print(CompanyModel.from_orm(co_orm))

