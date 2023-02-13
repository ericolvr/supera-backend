""" model class to products """
# pylint: disable=E0401
from sqlalchemy import Column, Integer, String, DateTime, Text, Numeric
from sqlalchemy.sql import func

from src.infra.configs.database import Base


class Product(Base):
    """product defintions"""

    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, index=True)
    price = Column(Numeric(10, 2))
    score = Column(Integer)
    image = Column(Text)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=True
    )
