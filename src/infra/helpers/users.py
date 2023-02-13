""" helpers to user """
# pylint: disable=E0401
from typing import Any
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.infra.models.users import User


class UserHelper:
    """ utilities for user """
    def __init__(self, database: Session):
        self.database = database

    async def filter_by_mobile(self, mobile: str) -> Any:
        """ to verify if user exists when token is requested """
        user = self.database.query(User).filter(
                User.mobile == mobile
        ).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User: {mobile} does not exist")

        return user
