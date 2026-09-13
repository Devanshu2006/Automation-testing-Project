def test_api_chaining(api_client):

    # 1. Get existing user
    get_response = api_client.get("/users/1")

    assert get_response.status == 200

    user = get_response.json()

    user_id = user["id"]

    print("User ID:", user_id)

    # 2. Get same user again using ID
    get_response_2 = api_client.get(f"/users/{user_id}")

    assert get_response_2.status == 200

    user_2 = get_response_2.json()

    assert user_2["id"] == user_id