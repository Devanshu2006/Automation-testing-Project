def test_api_chaining(api_client):

    # 1. Create User
    create_response = api_client.post(
        "/users",
        data={
            "name": "Devanshu",
            "username": "dev",
            "email": "dev@example.com"
        }
    )

    assert create_response.status == 201

    created_user = create_response.json()

    user_id = created_user["id"]

    print("Created User ID:", user_id)

    # 2. Get User
    get_response = api_client.get(
        f"/users/{user_id}"
    )

    assert get_response.status == 200

    # 3. Update User
    update_response = api_client.put(
        f"/users/{user_id}",
        data={
            "name": "Devanshu Updated",
            "username": "dev_updated",
            "email": "updated@example.com"
        }
    )

    assert update_response.status == 200

    updated_user = update_response.json()

    assert updated_user["name"] == "Devanshu Updated"

    # 4. Delete User
    delete_response = api_client.delete(
        f"/users/{user_id}"
    )

    assert delete_response.status == 200