from playwright.sync_api import expect


def test_authenticated_products(logged_in_page):
    page = logged_in_page

    page.goto(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        page.get_by_text("Products")
    ).to_be_visible()


def test_authenticated_cart(logged_in_page):
    page = logged_in_page

    page.goto(
        "https://www.saucedemo.com/inventory.html"
    )

    page.locator(
        ".inventory_item"
    ).first.get_by_role(
        "button",
        name="Add to cart"
    ).click()

    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("1")