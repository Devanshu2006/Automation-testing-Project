from playwright.sync_api import expect


def test_same_context_pages(browser):

    context = browser.new_context()

    page1 = context.new_page()
    page2 = context.new_page()

    page1.goto("https://www.saucedemo.com/")
    page2.goto("https://www.saucedemo.com/")

    # Login on page 1
    page1.locator("#user-name").fill("standard_user")
    page1.locator("#password").fill("secret_sauce")

    page1.get_by_role("button", name="Login").click()

    expect(page1).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    # Same context means storage/session state is shared.
    # Navigate page2 to the protected page.
    page2.goto(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(page2).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        page2.get_by_text("Products")
    ).to_be_visible()

    context.close()