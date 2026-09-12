import pytest
from api.test_data import USERS


@pytest.mark.parametrize("user", USERS)
def test_get_multiple_users(api_client, user):

    response = api_client.get(
        f"/users/{user['id']}"
    )

    assert response.status == 200

    data = response.json()

    assert data["id"] == user["id"]
    assert data["name"] == user["name"]
    assert data["email"] == user["email"]