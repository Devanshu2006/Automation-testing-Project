# from api.api_assertions import ApiAssertions


# def test_get_user(api_client):

#     response = api_client.get("/users/1")

#     ApiAssertions.assert_status(response, 200)
#     ApiAssertions.assert_success(response)
#     ApiAssertions.assert_json(response)

#     data = response.json()

#     assert data["id"] == 1
#     assert data["name"] != ""
#     assert data["email"] != ""
from api.api_assertions import ApiAssertions


def test_invalid_endpoint(api_client):

    response = api_client.get("/invalid-endpoint")

    ApiAssertions.assert_status(response, 404)