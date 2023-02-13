from httpx import AsyncClient

from src.main import app

create_user = {
    "fullname": "Johny Doe",
    "mobile": "11 900789267",
    "email": "johny@doe.com",
    "password": "johny12345",
    "role": "CLIENT",
}

login_user = {
    "mobile": "11 988776655",
    "password": "mary12345",
}


async def get_token():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        create_token = await ac.post("/authentication/token/", json=login_user)
        token = create_token.json()["access_token"]
        return token
