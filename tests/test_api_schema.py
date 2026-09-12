from api.api_schema import UserSchema


def test_user_schema(api_client):

    response = api_client.get("/users/1")

    assert response.status == 200

    data = response.json()

    UserSchema.validate(data)