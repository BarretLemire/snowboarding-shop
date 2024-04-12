import json
from fastapi import FastAPI
from enum import Enum
from models import Brand, Snowboard


with open("snowboards.json", "r") as f:
    snowboard_list = json.load(f)

app = FastAPI()

snowboard_list = list[Snowboard]

@app.get("/snowboards")
async def get_snowboards() -> list[Snowboard]:
    return snowboard_list.values()


@app.post("/snowboards/new")
async def new_snowboard(id: int, length: int, color: str, has_bindings: bool, Brand: Enum) -> list[Snowboard]:
    return snowboard_list.append(id)


@app.put("/snowboards/{id}")
async def update_snowboard(id: int, length: int, color: str, has_bindings: bool, brand: Enum) -> list[Snowboard]:
    updated_snowboard = snowboard_list[id]
    return id


@app.delete("/snowboards/{id}")
async def delete_snowboard(id: int) -> list[Snowboard]:
    snowboard_list.pop(id)
