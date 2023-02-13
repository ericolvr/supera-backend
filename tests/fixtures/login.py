import pytest


@pytest.fixture
def user_login():
    data = {
        "fullname": "Marie Jane",
        "email": "marie@jane.com",
        "password": "jan12345",
    }
    return data
    