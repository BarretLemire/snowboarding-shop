from pydantic import BaseModel
from enum import Enum

class Brand(Enum):
    brand: Enum

class Snowboard(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: Enum