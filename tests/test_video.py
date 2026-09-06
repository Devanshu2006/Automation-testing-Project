from playwright.sync_api import expect


def test_video_recording(page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Products")).to_be_visible()