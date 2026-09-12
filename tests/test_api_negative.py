def test_invalid_endpoint(playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.get("/invalid-endpoint")

    assert response.status == 404

    request.dispose()

def test_unauthorized_request(playwright):
    request = playwright.request.new_context(
        base_url="https://httpbin.org"
    )

    response = request.get("/bearer")

    assert response.status == 401

    request.dispose()