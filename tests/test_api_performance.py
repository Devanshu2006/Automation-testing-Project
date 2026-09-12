import time


def test_api_response_time(api_client):

    start_time = time.perf_counter()

    response = api_client.get("/users/1")

    end_time = time.perf_counter()

    response_time = end_time - start_time

    print(f"Response Time: {response_time:.3f} seconds")

    assert response.status == 200

    assert response_time < 2.0