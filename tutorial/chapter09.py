from fastapi import APIRouter

app09 = APIRouter()


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app09.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "ni":
        raise UnicornException(name=name)
    return {"unicorn_name": name}
