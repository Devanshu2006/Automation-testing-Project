def test_api_retry(api_client):

    response = api_client.get(
        "/users/1",
        retries=3
    )

    assert response.status == 200