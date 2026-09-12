import json
import pytest


def load_users():
    with open("data/users.json", "r") as file:
        return json.load(file)


@pytest.mark.parametrize("user", load_users())
def test_get_user_from_json(api_client, user):

    response = api_client.get(
        f"/users/{user['id']}"
    )

    assert response.status == 200

    data = response.json()

    assert data["id"] == user["id"]
    assert data["name"] == user["name"]
    assert data["email"] == user["email"]