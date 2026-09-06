import pytest
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def logged_in_page(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    yield page