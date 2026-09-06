import pytest
from playwright.sync_api import expect

from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.regression
def test_complete_purchase(logged_in_page):

    product_page = ProductPage(logged_in_page)

    product_page.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    product_page.open_cart()

    cart_page = CartPage(logged_in_page)

    cart_page.checkout()

    checkout_page = CheckoutPage(logged_in_page)

    checkout_page.fill_customer_details(
        "Dev",
        "Girare",
        "411001"
    )

    checkout_page.continue_checkout()

    expect(
        logged_in_page.get_by_text(
            "Checkout: Overview"
        )
    ).to_be_visible()

    checkout_page.finish_order()

    expect(
        checkout_page.success_message
    ).to_be_visible()