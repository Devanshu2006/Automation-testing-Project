def test_get_user(api_request):
    response = api_request.get("/users/1")

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] != ""