import time
from playwright.sync_api import Page, Route

mock_network_data = {"data": [], "message": "No Orders"}


def intercept_mocking_the_network_by_using_fake_response_from_server(route: Route):
    route.fulfill(json=mock_network_data)


def test_mocking_network_and_get_response_of_empty_order_but_actual_there_is_order(page: Page):

    page.route(
        "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
        intercept_mocking_the_network_by_using_fake_response_from_server
    )

    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_placeholder("email@example.com").fill("nazmul2811@diu.edu.bd")
    page.locator("#userPassword").fill("Rh@r12345512")

    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    without_order_message = page.locator(".mt-4.ng-star-inserted").text_content()
    print(without_order_message)

    time.sleep(1)
    page.close()
