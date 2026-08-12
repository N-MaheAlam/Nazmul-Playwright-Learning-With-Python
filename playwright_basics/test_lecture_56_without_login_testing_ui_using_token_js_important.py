import time

from playwright.sync_api import Playwright, expect

from playwright_basics.utils.api_utils_lecture_49_50_51_important import APIValidationFirstClass


def test_login_without_credential_using_token_generated_from_api_utils(playwright: Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    # creating an instance of the class from where we will collect the token
    token_from_this_class = APIValidationFirstClass()
    # using object calling the method to get the token of the login credentials that we generated
    # by api calls in function "token_for_login_details" in file placed in "utils" folder name
    # "api_utils_lecture_49_50_51_60_important.py"
    get_token_from_utils_api_validation_class = token_from_this_class.token_for_login_details(playwright)
    # "add_init_script" is used to javascript code in our playwright code. the three apostrophe
    # (""" javascript code """) is used to define the javascript code. In the script, we are going inside the
    # local storage of our browser and set up the value of token which is nothing but came from
    # the function "token_for_login_details(playwright)" in lecture 49-50-51 file
    page.add_init_script(f"""localStorage.setItem('token','{get_token_from_utils_api_validation_class}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()

    # expecting the below visible text
    expect(page.locator
           (':text("* If orders Will be more than 7 your last order will get deleted")')).to_be_visible()
    time.sleep(2)

