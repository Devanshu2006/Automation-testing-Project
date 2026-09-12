from playwright.sync_api import expect


def test_get_users(playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.get("/users")

    expect(response).to_be_ok()

    assert response.status == 200

    data = response.json()

    assert len(data) > 0
    assert "name" in data[0]
    assert "email" in data[0]

    request.dispose()

def test_create_user(playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.post(
        "/users",
        data={
            "name": "Dev",
            "username": "devanshu",
            "email": "dev@example.com"
        }
    )

    expect(response).to_be_ok()

    assert response.status == 201

    data = response.json()

    assert data["name"] == "Dev"
    assert data["username"] == "devanshu"
    assert data["email"] == "dev@example.com"

    request.dispose()

def test_update_user_put(playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.put(
        "/users/1",
        data={
            "name": "Devanshu",
            "username": "dev",
            "email": "dev@example.com"
        }
    )

    expect(response).to_be_ok()

    assert response.status == 200

    data = response.json()

    assert data["name"] == "Devanshu"
    assert data["username"] == "dev"
    assert data["email"] == "dev@example.com"

    request.dispose()

def test_update_user_patch(playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.patch(
        "/users/1",
        data={
            "email": "newemail@example.com"
        }
    )

    expect(response).to_be_ok()

    assert response.status == 200

    data = response.json()

    assert data["email"] == "newemail@example.com"

    request.dispose()

def test_delete_user(playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.delete("/users/1")

    assert response.status == 200

    request.dispose()