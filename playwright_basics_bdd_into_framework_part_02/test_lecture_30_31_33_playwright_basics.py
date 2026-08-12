# This import is  "Page" used to skip this below line
# -------------------------
# browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
# --------------------------------
# However this works only in Chrome and Microsoft Edge browser. If we want to  use in other browsers and
# want to modify our browser before opening, we need to use the above code
# then we need to write the above code
import time

from playwright.sync_api import Page, expect, Playwright


# ---------------------------- LECTURE 30 ------------------------

# here in the argument "playwright" is a built-in fixture that comes from the plugin
# "pytest-playwright" that we have installed at the first using command prompt
def test_my_first_browser_check(playwright):
    # playwright calling chromium engine and launching it and
    # "headless = False" mean it will open in browser. If headless in True or
    # nothing is given as argument that it will run chromium engine without launching the
    # browsers
    browser = playwright.chromium.launch(headless=False)
    # "new_context()" open browser separately in i
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.close()


# ---------------------------- LECTURE 31 ------------------------

# Calling the "Page" class from "playwright.sync_api"
# In RUN button we when we click, we will see "Modify Run Configuration"
# Go inside that and in "argument" put "--headed" so that this test runs in headed mode
# And also if we want to run it in terminal headed mode just write the below code from this directory
# " pytest test_lecture_30_31_33_playwright_basics.py :: test_second_browser_check_shortcut -- headed "
def test_second_browser_check_shortcut(page: Page):
    page.goto("https://www.facebook.com/")
    print("Hello, This is a  Playwright code ")
    page.close()


# ---------------------------- LECTURE 33 & 34 ------------------------

def test_rahul_shetty_academy_login_page_input_values(page: Page):
    # go to this below link
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    # find this label and put "rahulshettyacademy"
    # However, get_by_label works in certain condition. Whenever we identify a label, make sure
    # it has a label tag (inspect element then you can see). Then, the edit box where we put the
    # value for example "("rahulshettyacademy")" should be inside the label. The edit box could be an
    # input tag which refers to HTML. or the label should have a "for" attribute that will be used
    # as "id" in input tag if input is written separately outside label.
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")

    # when we want to select something from a predefined box use "combobox" and select the option
    # using "value" tag html
    page.get_by_role("combobox").select_option("consult")

    # using css to locate. for "id" we use "#name_of_the_id" and if we want to select by class use
    #  ".class_name". Now, click on the checkbox using "check()" function
    page.locator("#terms").check()

    page.get_by_role("link", name="terms and conditions").click()
    # Button is used as argument and we selected the text of that button. Here we can see it is
    # "Sign In" text inside the button
    page.get_by_role("button", name="Sign In").click()
    time.sleep(5)
    page.close()
