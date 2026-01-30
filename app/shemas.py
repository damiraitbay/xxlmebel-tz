from pydantic import BaseModel 
from typing import List

class FurnitureOut(BaseModel):
    id: int
    name: str
    price: float
    category: str

    class Config:
        from_attributes=True
class OrderCreate(BaseModel):
    email: str
    items: List[int]

class OrderOut(BaseModel):
    id: int
    email: str
    total_price: float

    class Config:
        from_attributes=True

        