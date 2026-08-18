import time

from playwright.sync_api import Page, Route


# https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69f50fdff86ba51a65995281

def get_the_order_id_of_another_user(route: Route):

    route.continue_(url=
                    "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=69f51d0ef86ba51a659960a8")


def test_view_oder_users_order_that_blocks_this_user_to_view(page: Page):
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*",
               get_the_order_id_of_another_user)

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("nazmul2811@diu.edu.bd")
    page.locator("#userPassword").fill("Rh@r12345512")
    page.get_by_role("button", name="Login").click()
    # Till this is the basic log in and view orders
    page.get_by_role("button", name="ORDERS").click()

    # when we click on this "View button" in generate the url
    # "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*" and the "route" grabs it's
    # and follows the "get_the_order_id_of_another_user" function. In previous lecture what we did?
    # we did like we got the order details response from the server, but we change it and send our
    # made response [mock] that browser thought came from server and generated no orders html page. but here
    # When customer clicks on view the order for a specific order it generates a link
    # "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id= exact_order_id_for_that
    # _customer" with the order of that
    # customer. But we are going change the url like "https://rahulshettyacademy.com/api/ecom/order
    # /get-orders-details?id= order_id_of_another customer_who_does_not_have_this_log_in_permission"
    # that means last time we changed the response of server, but now we are requesting server with a
    # dummy url which is invalid for this customer and server should show reply an error json
    # which will help to pop up the below html in server
    # " You do not have authorization for this order"
    # Final means before it reaches server we are mocking and in last lecture we mocked the response
    # that we got from server.
    page.get_by_role("button", name="View").first.click()
    unauthorised_message = page.locator(".blink_me").text_content()
    print(unauthorised_message)
    time.sleep(3)
