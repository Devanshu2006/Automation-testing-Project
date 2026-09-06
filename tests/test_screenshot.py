from playwright.sync_api import expect


def test_screenshot_on_failure(page):
    page.goto("https://www.saucedemo.com/")

    username = page.locator("#user-name")

    username.fill("standard_user")

    # Intentionally wrong assertion
    expect(username).to_have_value("wrong_value")