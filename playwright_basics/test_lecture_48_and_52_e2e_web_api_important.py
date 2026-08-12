import time

from playwright.sync_api import Playwright, expect

from playwright_basics.utils.api_utils_lecture_49_50_51_important import APIValidationFirstClass


# --------------------- Lecture 48 first building UI Automation for API test ------------------------------
# If we are using "Page" class then the argument will be
# def test_e2e_web_api_check(page: Page):
# But we are using the playwright and opening chrome, page manually. So, use the below format of
# argument
def test_e2e_web_api_check(playwright: Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("nazmul2811@diu.edu.bd")
    page.locator("#userPassword").fill("Rh@r12345512")
    # Till this point from the top of this function is just regular log in info providing
    # and clicking the log in button
    page.get_by_role("button", name="Login").click()
    time.sleep(1)

    # ------------------ LECTURE 52 --  calling the API class to use it in tests --------
    # Creating an object for the "APIValidationFirstClass" which comes from
    # "api_utils_lecture_49_50_51_60_important.py", this file
    creating_order_class = APIValidationFirstClass()
    # Using the object when we call the method "create_order_api_validation_rahul_shetty"
    # It provides the "order_id" that has been collected using API call
    order_id = creating_order_class.create_order_api_validation_rahul_shetty(playwright)

    # -------------------- LECTURE 52 ---- Dynamically checking order id sent from apis ----------
    # Now, click the "ORDERS" button
    page.get_by_role("button", name="ORDERS").click()
    # Using locator we are filter the "tr" [table rows] which as the "order_id" that we got from
    # the api class call and the scope is now giving in " order_row" which means now if we perform
    # any operation in "order_row" like, click, visible whatever playwright code, it will be limited only
    # that order row only
    order_row = page.locator("tr").filter(has_text=order_id)
    # click the view button only on that specific table row
    order_row.get_by_role("button", name="View").click()
    # We are expecting that the below text should be there
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    # collecting the order_id from UI
    order_id_from_ui = page.locator(".col-text.-main").text_content()
    # printing the order_id from UI in console
    print("Order Id from UI: ", order_id_from_ui)
