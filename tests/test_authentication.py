import pytest
from httpx import AsyncClient
from src.main import app


user = {
    "mobile": "11 988776655",
    "password": "mary12345"
}


@pytest.mark.asyncio()
async def test_generate_token():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/authentication/token/", json=user)
        assert response.status_code == 201
