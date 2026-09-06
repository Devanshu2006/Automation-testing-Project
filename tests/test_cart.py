from playwright.sync_api import expect

from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_product_cart_workflow(logged_in_page):

    product_page = ProductPage(logged_in_page)

    expect(product_page.page_title).to_be_visible()

    product_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    product_page.open_cart()

    cart_page = CartPage(logged_in_page)

    expect(cart_page.cart_items).to_have_count(1)

    products = cart_page.get_product_names()

    assert "Sauce Labs Backpack" in products