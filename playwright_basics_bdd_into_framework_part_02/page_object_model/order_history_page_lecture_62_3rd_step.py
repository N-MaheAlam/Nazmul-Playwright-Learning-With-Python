from playwright_basics_pom_into_framework_part_01.page_object_model.my_specific_order_details_page_4th_step import \
    OrderDetailsPage


class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def view_the_actual_order_details(self, order_id):
        order_row = self.page.locator("tr").filter(has_text=order_id)

        order_row.get_by_role("button", name="View").click()
        order_details_object = OrderDetailsPage(self.page)
        return order_details_object
