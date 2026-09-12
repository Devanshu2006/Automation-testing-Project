import json


def test_update_user(api_client):

    with open("data/update_user.json", "r") as file:
        payload = json.load(file)

    response = api_client.put(
        "/users/1",
        data=payload
    )

    assert response.status == 200

    data = response.json()

    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]