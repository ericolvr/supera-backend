""" schema to products """
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class ProductSchema(BaseModel):
    """ data definitions """
    name: str
    price: Decimal
    score: int
    image: str

    class Config:
        """ set orm mode """
        orm_mode=True
        
        
class ProductUpdate(ProductSchema):
    """ data definitions """
    name: Optional[str] = None
    price: Optional[float] = None
    score: Optional[int] = None
    image: Optional[str] = None
    