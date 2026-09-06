from playwright.sync_api import Page


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")

        self.continue_button = page.get_by_role(
            "button",
            name="Continue"
        )

        self.finish_button = page.get_by_role(
            "button",
            name="Finish"
        )

        self.success_message = page.get_by_text(
            "Thank you for your order!"
        )

    def fill_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_order(self):
        self.finish_button.click()