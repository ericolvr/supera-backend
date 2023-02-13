""" schema to products """
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class CartSchema(BaseModel):
    """data definitions"""

    user_id: Optional[int] = None
    product_id: int
    product_name: str
    product_price: Decimal
    quantity: int
    status: int
    subtotal: Optional[Decimal] = None
    total: Optional[Decimal] = None

    class Config:
        """set orm mode"""

        orm_mode = True


class CartUpdate(CartSchema):
    """data definitions"""

    user_id: Optional[int] = None
    product_id: Optional[int] = None
    product_name: Optional[str] = None
    product_price: Optional[Decimal] = None
    quantity: Optional[int] = None
    status: Optional[int] = None
