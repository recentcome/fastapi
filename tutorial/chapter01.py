from enum import Enum

from fastapi import APIRouter, Path

app01 = APIRouter()


@app01.get('/hello/{path}')
def hello(path: str):
    return {'message': path}


@app01.get('/path/paras')
def path_params01():
    return {'messages': "this is messages"}


@app01.get('/path/{paras}')
def path_params01(params):
    return {'messages': params}


class CityInfo(str, Enum):
    Beijing = "Beijing city"
    Shanghai = "Shanghai city"


@app01.get('/path_city/{city}')
def path_getcity(city: CityInfo):
    if city == CityInfo.Shanghai:
        return {'city_name': city, 'confirmed': 1234, 'dead': 8}
    if city == CityInfo.Beijing:
        return {'city_name': city, 'confirmed': 355, 'dead': 6}
    else:
        return {'city_name': city, 'confirmed': None, 'dead': None}


@app01.get('/path_file/{file_path:path}')       # 文件路径参数校验
def path_file(file_path: str):
    return file_path
