import json
from fastapi import FastAPI, HTTPException
from enum import Enum
from typing import List
from models import Brand, Snowboard, NewSnowboard


app = FastAPI()

with open("snowboards.json", "r") as f:
    snowboard_data = json.load(f)
    snowboard_list = [Snowboard(**snowboard) for snowboard in snowboard_data]


@app.get("/snowboards", response_model=List[Snowboard])
async def get_snowboards() -> list[Snowboard]:
    return snowboard_list


@app.post("/snowboards/new", response_model=Snowboard)
async def new_snowboard(snowboard: NewSnowboard) -> Snowboard:
    new_snowboard = Snowboard(**snowboard.dict())
    snowboard_list.append(new_snowboard)
    return new_snowboard


@app.put("/snowboards/{id}")
async def update_snowboard(id: int, length: int, color: str, has_bindings: bool, brand: Brand) -> Snowboard:
    for snowboard in snowboard_list:
        if snowboard.id == id:
            snowboard.length = length
            snowboard.color = color
            snowboard.has_bindings = has_bindings
            snowboard.brand = brand
            return snowboard
    raise HTTPException(status_code=404, detail="Snowboard not found")



@app.delete("/snowboards/{id}")
async def delete_snowboard(id: int) -> Snowboard:
    for index, snowboard in enumerate(snowboard_list):
        if snowboard.id == id:
            deleted_snowboard = snowboard_list.pop(index)
            return deleted_snowboard
    raise HTTPException(status_code=404, detail="Snowboard not found")
