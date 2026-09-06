import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(page.get_by_text("Products")).to_be_visible()