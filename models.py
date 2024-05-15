from pydantic import BaseModel
from enum import Enum

class Brand(str, Enum):
    Burton = "Burton"
    Nitro = "Nitro"
    Saloman = "Saloman"

class Snowboard(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: Brand

class NewSnowboard(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: Brand