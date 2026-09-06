from playwright.sync_api import expect


def test_context_isolation(browser):

    context1 = browser.new_context()
    context2 = browser.new_context()

    page1 = context1.new_page()
    page2 = context2.new_page()

    page1.goto("https://www.saucedemo.com/")
    page2.goto("https://www.saucedemo.com/")

    # Login only in Context 1
    page1.locator("#user-name").fill("standard_user")
    page1.locator("#password").fill("secret_sauce")
    page1.get_by_role("button", name="Login").click()

    # Context 1 should be logged in
    expect(page1).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Context 2 should still be on login page
    expect(
        page2.get_by_role("button", name="Login")
    ).to_be_visible()

    context1.close()
    context2.close()