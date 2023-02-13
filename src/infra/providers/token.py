""" jwt token """
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt

load_dotenv()

vars_token = {
    "secret_key": 'kjwqdwq9&__MD9mjs6s,s88s78s',
    "algorithm": 'HS256',
    "expires": 120
}


class TokenProvider:
    """ provide token to authenticate user """
    @staticmethod
    async def create_access_token(data: dict):
        """ generate access_token  """
        user_data = data.copy()
        expires = datetime.utcnow() + timedelta(hours=int(vars_token["expires"]))

        user_data.update({"exp": expires})
        jwt_token = jwt.encode(
            user_data, vars_token["secret_key"], algorithm=vars_token["algorithm"]
        )
        return jwt_token

    @staticmethod
    async def verify_access_token(token: str):
        """ verify if is a valid token  """
        payload = jwt.decode(
            token, vars_token["secret_key"], algorithms=[vars_token["algorithm"]]
        )
        return payload.get("sub")
