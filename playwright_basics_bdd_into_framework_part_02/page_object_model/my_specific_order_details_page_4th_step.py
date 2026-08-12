from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self, page):
        self.page = page

    def verify_the_thank_you_message(self):
        expect(self.page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")

        order_id_from_ui = self.page.locator(".col-text.-main").text_content()
        print("Order Id from UI: ", order_id_from_ui)
