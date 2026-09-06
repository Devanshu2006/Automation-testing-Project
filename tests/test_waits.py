from playwright.sync_api import expect


def test_playwright_auto_wait(page):

    page.goto("https://www.saucedemo.com/")

    username = page.locator("#user-name")

    expect(username).to_be_visible()

    username.fill("standard_user")

    expect(username).to_have_value("standard_user")