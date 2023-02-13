""" schema to products """
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class PurchaseSchema(BaseModel):
    """data definitions"""

    user_id: int
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
