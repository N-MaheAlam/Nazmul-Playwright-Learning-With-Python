from playwright_basics_pom_into_framework_part_01.page_object_model.order_history_page_lecture_62_3rd_step import \
    OrderHistoryPage


class Dashboard:
    def __init__(self, page):
        self.page = page

    def click_on_order_button(self):
        self.page.get_by_role("button", name="ORDERS").click()
        order_history_page_object = OrderHistoryPage(self.page)
        return order_history_page_object
