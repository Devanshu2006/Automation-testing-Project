# import pytest
# from pages.login_page import LoginPage


# @pytest.fixture(scope="function")
# def logged_in_page(page):
#     login_page = LoginPage(page)

#     login_page.open()
#     login_page.login(
#         "standard_user",
#         "secret_sauce"
#     )

#     yield page

import pytest
from config import API_TOKEN
from config import API_BASE_URL
from api.api_client import ApiClient


@pytest.fixture
def api_request(playwright):
    request = playwright.request.new_context(
        base_url=API_BASE_URL
    )

    yield request

    request.dispose()


@pytest.fixture
def api_client(api_request):
    return ApiClient(
        api_request,
        token=API_TOKEN
    )