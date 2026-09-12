def test_get_user(api_client):

    response = api_client.get("/users/1")

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] != ""
    assert data["email"] != ""