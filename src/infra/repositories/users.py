""" user repository """
# pylint: disable=E0401
from typing import Any
from fastapi import HTTPException, status
from sqlalchemy import or_
from sqlalchemy.orm import Session

from api.schemas.users import UserInput
from src.infra.models.users import User
from src.infra.providers.hash import HashProvider


class UserRepository:
    """user repository"""

    def __init__(self, database: Session):
        self.database = database

    async def create_user(self, user: UserInput) -> User:
        """create user"""
        await UserRepository(self.database).check_exists(user.email, user.mobile)

        new = User(
            fullname=user.fullname,
            email=user.email,
            mobile=user.mobile,
            password=await HashProvider.make_hash(user.password),
            role=user.role,
        )

        self.database.add(new)
        self.database.commit()
        self.database.refresh(new)

        return new

    async def check_exists(self, email: str, mobile: str) -> Any:
        """check if mobile or email already exists"""
        user = (
            self.database.query(User)
            .filter(or_(User.email == email, User.mobile == mobile))
            .first()
        )

        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User Email or Mobile already exists",
            )
        return

    async def list_all(self, offset: int, limit: int):
        """list all users - paginated"""
        users = self.database.query(User).offset(offset).limit(limit).all()
        return users

    async def list_by_role(self, role: str, offset: int, limit: int):
        """list users by role type"""
        users = (
            self.database.query(User)
            .filter(User.role == role)
            .offset(offset)
            .limit(limit)
            .all()
        )
        return users
