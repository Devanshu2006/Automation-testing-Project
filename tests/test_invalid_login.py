from playwright.sync_api import expect


def test_invalid_login(page):

    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("wrong_user")
    page.locator("#password").fill("wrong_password")

    page.get_by_role("button", name="Login").click()

    error = page.locator("[data-test='error']")

    expect(error).to_be_visible()

    expect(error).to_contain_text("Username and password do not match")