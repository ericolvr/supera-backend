""" hashs for user """
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class HashProvider:
    """make hashs from user password"""

    @staticmethod
    async def make_hash(password):
        """make hash to users password"""
        return pwd_context.hash(password)

    @staticmethod
    async def verify_hash(password, user_hash):
        """verify hash to generate user token"""
        return pwd_context.verify(password, user_hash)
