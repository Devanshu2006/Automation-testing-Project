import pytest
def test_authenticated_api(api_request):

    response = api_request.get(
        "https://httpbin.org/bearer"
    )

    assert response.status == 200

    data = response.json()

    assert data["authenticated"] is True

@pytest.fixture
def auth_api_request(playwright):

    headers = {
        "Authorization": "Bearer my-test-token"
    }

    request = playwright.request.new_context(
        base_url="https://httpbin.org",
        extra_http_headers=headers
    )

    yield request

    request.dispose()

def test_authenticated_api(auth_api_request):

    response = auth_api_request.get("/bearer")

    assert response.status == 200

    data = response.json()

    assert data["authenticated"] is True