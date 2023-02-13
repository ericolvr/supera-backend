import pytest
from httpx import AsyncClient
from src.main import app
from tests.utils import login_user, get_token

record = {
    "name": "Product Test One",
    "price": 12.00,
    "score": "90",
    "image": "home/path.png"
}


@pytest.mark.asyncio
async def test_create_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/products/", json=record)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_duplicate_product():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/products/", json=record)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_list_products():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_list_products_pagination():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products/?offset=0&limit=100")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_list_products_pagination_limit():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/products/?offset=0&limit=1")
        count_result = len(response.json())
    assert count_result == 1


@pytest.mark.asyncio
async def test_list_products_offset_pagination():
    async with AsyncClient(app=app, base_url="http://test") as ax: # cache -> check
        response = await ax.get("/products/?offset=1&limit=1")
        product = response.json()[0]["name"]
    assert product == "lapis"


@pytest.mark.asyncio
async def test_update_by_name():
    async with AsyncClient(app=app, base_url="http://test") as aac:
        token = await get_token()
        response = await aac.patch(
            "/products/update/Product Test One", 
            json={"name": "Product-Updated"},
            headers={
                "Authorization": f"Bearer {token}"
            },
        )

        product = response.json()["name"]
    assert product == "Product-Updated"


@pytest.mark.asyncio
async def test_delete_by_name():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        token = await get_token()
        response = await ac.delete(
            "/products/delete/Product-Updated",
            headers={
                "Authorization": f"Bearer {token}"
            },
        )
    assert response.status_code == 204
