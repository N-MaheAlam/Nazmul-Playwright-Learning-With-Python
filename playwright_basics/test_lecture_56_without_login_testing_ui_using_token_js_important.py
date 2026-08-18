import time

from playwright.sync_api import Playwright, expect

from playwright_basics.utils.api_utils_lecture_49_50_51_important import APIValidationFirstClass

# last 54-55 lecture was about mocking response, request network using route. Now, if we want to
# run a javascript before running the javascript of the page or UI, we can use "add_init_script"
# built in method.
'''
                            Feature	route()	        add_init_script()
Controls network requests	    ✅   	                    ❌
        Mock API response	    ✅	                        ❌
            Block request	    ✅	                        ❌
        Modify API request	    ✅	                        ❌
        Inject JavaScript	    ❌	                        ✅
        Runs before page JS	    ❌	                        ✅
Modify browser environment	    ❌	                        ✅
Set browser/page variables	    ❌	                        ✅


EASY way to remember route controls network and aa_init_script controls javascript
'''


def test_login_without_credential_using_token_generated_from_api_utils(playwright: Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    # creating an instance of the class from where we will collect the token
    token_from_this_class = APIValidationFirstClass()
    # using object calling the method to get the token of the login credentials that we generated
    # by api calls in function "token_for_login_details" in file placed in "utils" folder name
    # "api_utils_lecture_49_50_51_60_important.py"
    get_token_from_utils_api_validation_class = token_from_this_class.token_for_login_details(playwright)
    # "add_init_script" is used to javascript code in our playwright code before running the javascript
    # code of the UI. the three apostrophe
    # (""" javascript code """) is used to define the javascript code. In the script, we are going inside the
    # local storage of our browser and set up the value of token which is nothing but came from
    # the function "token_for_login_details(playwright)" in lecture 49-50-51 file. This localStorege is
    # when we inspect element we can navigate Application -> local storage where we set the value token
    # because if we set the token, we do not need to log in everytime to perform some functions that
    # require login which takes every 4-5 seconds every time. "localStorege" can set , get items in our
    # local storage [web application local store not the computer].
    # Here the below code "f" means there might be varibles in {} curly braces, """"""" inside this
    # 6 apostrophe we provide our javascript code. "localStorage.setItem" is setting the token key and
    # its value in our browser before loading the "page.goto("https://rahulshettyacademy.com/client")"
    # helping us not to log in every time. Then it is directly landing in home page and we are
    # clicking ORDERS button and verifying the message is present or not
    page.add_init_script(f"""localStorage.setItem('token','{get_token_from_utils_api_validation_class}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()

    # expecting the below visible text
    expect(page.locator
           (':text("* If orders Will be more than 7 your last order will get deleted")')).to_be_visible()
    time.sleep(2)
