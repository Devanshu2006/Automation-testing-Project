from playwright.sync_api import expect


def test_response_validation(playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.get("/users/1")

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] != ""
    assert data["username"] != ""
    assert data["email"] != ""

    request.dispose()

def test_response_data_types(playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.get("/users/1")

    assert response.status == 200

    data = response.json()

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["username"], str)
    assert isinstance(data["email"], str)

    request.dispose()