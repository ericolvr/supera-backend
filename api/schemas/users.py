""" schema to user """
from typing import Optional
from pydantic import BaseModel


class UserInput(BaseModel):
    """data definitions"""

    fullname: str
    email: str
    mobile: str
    password: str
    role: str

    class Config:
        """set orm mode"""

        orm_mode = True


class UserUpdate(BaseModel):
    """user schema to update"""

    fullname: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserAuth(BaseModel):
    """user schema to generate token"""

    mobile: str
    password: str


class UserAuthenticated(BaseModel):
    fullname: str
    """ user schema to response access_token """
    mobile: str
    access_token: str
