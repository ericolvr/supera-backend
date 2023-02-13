import pytest
from httpx import AsyncClient
from src.main import app


cart = {
    "product_id": 11,
    "product_name": "caneta",
    "product_price": 10.00,
    "quantity": 1,
    "status": 0,
}

@pytest.mark.asyncio
async def test_add_to_cart():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/cart/", json=cart)
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_list_in_localstorage_cart():
    items = '[131, 132, 133, 134]'
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(f"/cart/items/{items}")

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_by_id():
    async with AsyncClient(app=app, base_url="http://test") as ac:

        response = await ac.post(
            "/cart/update/131", 
            json={"quantity": 89},
        )
        cart = response.json()["quantity"]
    assert cart == 89