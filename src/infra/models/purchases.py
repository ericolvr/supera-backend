""" model class to cart """
from enum import IntEnum
from sqlalchemy import Column, Integer, String, DateTime, Enum, Numeric
from sqlalchemy.sql import func

from src.infra.configs.database import Base


class EnumStatus(IntEnum):
    UNPROCESSED = 0
    PROCESSED = 1
    
class Purchase(Base):
    __tablename__ = "purchases"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    products = Column(Integer)
    total = Column(Numeric(10, 2))
   
    quantity = Column(Integer)
    status = Column(Enum(EnumStatus))

    created_at = Column(DateTime(timezone=True), 
        server_default=func.now(), nullable=True)
    