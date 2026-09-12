from playwright.sync_api import expect
from pages.product_page import ProductPage


def test_add_product_to_cart(logged_in_page):
    page = logged_in_page

    page.goto("https://www.saucedemo.com/inventory.html")

    product_page = ProductPage(page)

    expect(product_page.page_title).to_be_visible()

    product_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    expect(product_page.cart_badge).to_have_text("1")