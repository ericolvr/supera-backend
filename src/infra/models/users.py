""" model class to user """
# pylint: disable=E0401
from enum import IntEnum
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func

from src.infra.configs.database import Base


class EnumStatus(IntEnum):
    """ user types """
    CLIENT = 0
    ADMIN = 1
    
class User(Base):
    """ user defintions """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    fullname = Column(String(100), unique=True, index=True)
    mobile = Column(String(20), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    role = Column(Enum(EnumStatus))
    created_at = Column(DateTime(timezone=True),
                        server_default=func.now(), nullable=True)
    
