# ------------- Lecture 53 -----------------
# when we go to https://rahulshettyacademy.com/client/#/dashboard/myorders after log in I mean
# when we log in than go to the orders page we have already orders. However, If there is no order
# then the UI should show a message like " There is no order come back later please".
# Now, we do not want to remove our orders from the order page but to show this message. How could we
# show that. That's where we will mock the response ( give a made response that will trigger
# you have no order page but order will be there. But when we will test it will show the UI
#  how will look it there is no response )from the network
import time


# ------------- Lecture 54 sending mock response as if it is sent by server as response -----------------

# How the process normally works
# -> 1)  we use API calls from browser ['''page.get_by_role("button", name="ORDERS").click()''''']
# -> 2) API calls connect server and returns back with response from server and on that response
# we are sending {"data": [], "message": "No Orders"} to the browser. Once browser have this response
# then it generates UI or html page for that mock response. In UI, we get " there is no order"
# somthing like that response. Now, we grab the text and shows in browser
# -> ['''page.locator(".mt-4.ng-star-inserted").text_content()']
# -> 3) With that response, browsers generates UI based on that response.

# So what we do, we fake the response that we get from server
import time
from playwright.sync_api import Page, Route

mock_network_response_data = {"data": [], "message": "No Orders"}


def intercept_mocking_the_network_by_using_fake_response_from_server(route: Route):
    # when we click on "ORDERS" server provides all the order list in json format and browser collects
    # it and arrange the html of order list. However, in the response of server which are nothing but
    # order list in json format, we are mocking means,telling the browser that server gives us this
    # repose "mock_network_response_data = {"data": [], "message": "No Orders"}" and fulfill my request.
    # browser thinks there is no order so the html is different, and it generates the no order html
    # Now check into this line
    # "without_order_message = page.locator(".mt-4.ng-star-inserted").text_content().strip()"
    route.fulfill(json=mock_network_response_data)


def test_mocking_network_and_get_response_of_empty_order_but_actual_there_is_order(page: Page):
    # So the route listening the tests and when it founds any link like below format, it goes to the
    # event "intercept_mocking_the_network_by_using_fake_response_from_server" which is a function
    # the "*" in link means after the "get-orders-for-customer/" resource there can be anything but when
    # its found the https://rahulshettyacademy.com/api/ecom/order/
    # get-orders-for-customer/_any_extra_resouces_we_don't_need_to_match_but_the first_part
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",
               intercept_mocking_the_network_by_using_fake_response_from_server
               )
    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_placeholder("email@example.com").fill("nazmul2811@diu.edu.bd")
    page.locator("#userPassword").fill("Rh@r12345512")

    page.get_by_role("button", name="Login").click()
    # When we click on the "ORDERS" then the url
    # "https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*" pops up and "route"
    # grab it instantly and perform whatever is instructed
    page.get_by_role("button", name="ORDERS").click()
    # Once browsers gets the mock response, then it generates the no order page
    # and from there we grab the text "You have No Orders to show at this time. Please Visit Back Us"
    # and removes any space from left and right using "strip()" function
    without_order_message = page.locator(".mt-4.ng-star-inserted").text_content().strip()
    # Print the message in console
    print("\n The message of empty orders: ", without_order_message)

    time.sleep(1)
    page.close()
