import pytest
from httpx import AsyncClient
from src.main import app
from utils import create_user, get_token


@pytest.mark.asyncio
async def test_create_user():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/users/", json=create_user)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_list_users():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        token = await get_token()
        response = await ac.get(
            "/users/",
            headers={"Authorization": f"Bearer {token}"},
        )
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_list_user_pagination_limit():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        token = await get_token()
        response = await ac.get(
            "/user/?offset=0&limit=1",
            headers={"Authorization": f"Bearer {token}"},
        )
        count_result = len(response.json())
    assert count_result == 1


@pytest.mark.asyncio
async def test_list_user_offset_pagination():
    async with AsyncClient(app=app, base_url="http://test") as ax: # cache -> check
        token = await get_token()
        response = await ax.get(
            "/users/?offset=1&limit=1",
            headers={"Authorization": f"Bearer {token}"},
        )
        user = response.json()[0]["fullname"]
    assert user == "John Doe"


# async def get_token():
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         create_token = await ac.post("/authentication/token/", json=user)
#         token = create_token.json()["access_token"]
#         return token