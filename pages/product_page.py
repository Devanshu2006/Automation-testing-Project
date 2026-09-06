from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page

        # Page elements
        self.page_title = page.get_by_text("Products")
        self.cart_link = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def is_product_page_visible(self):
        return self.page_title.is_visible()

    def select_product(self, product_name):
        self.page.get_by_text(product_name, exact=True).click()

    def add_product_to_cart(self, product_name):
        product = self.page.locator(
            ".inventory_item",
            has_text=product_name
        )

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def get_cart_count(self):
        return self.cart_badge.inner_text()

    def open_cart(self):
        self.cart_link.click()