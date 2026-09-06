from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role(
            "button",
            name="Checkout"
        )
        self.continue_shopping_button = page.get_by_role(
            "button",
            name="Continue Shopping"
        )

    def get_product_names(self):
        return self.page.locator(
            ".inventory_item_name"
        ).all_inner_texts()

    def checkout(self):
        self.checkout_button.click()

    def continue_shopping(self):
        self.continue_shopping_button.click()