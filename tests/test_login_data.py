import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from test_data import LOGIN_TEST_DATA


@pytest.mark.parametrize(
    "username, password, expected_success",
    LOGIN_TEST_DATA
)
def test_login_with_multiple_data(
    page,
    username,
    password,
    expected_success
):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(username, password)

    if expected_success:

        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        expect(
            page.get_by_text("Products")
        ).to_be_visible()

    else:

        expect(
            login_page.error_message
        ).to_be_visible()