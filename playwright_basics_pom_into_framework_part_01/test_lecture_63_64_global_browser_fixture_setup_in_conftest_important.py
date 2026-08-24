import json
import time
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import browser

from playwright_basics_pom_into_framework_part_01.page_object_model.dashboard_page_lecture_61_62__2nd_step import \
    Dashboard
from playwright_basics_pom_into_framework_part_01.page_object_model.login_page_lecture_61_1st_step import LoginPage
from playwright_basics_pom_into_framework_part_01.utils.api_utils_lecture_49_50_51_60_important import \
    APIValidationFirstClass

''' Writing multiple comments line using triple single or double quote
{
  "user_credentials" : [
    {
      "user_email": "nazmul2811@diu.edu.bd",
      "user_password": "Rh@r12345512"


    },
    {
      "user_email": "anshika@gmail.com",
      "user_password": "Iamking@000"
    }
  ]
}

The above code we can say like this way 
{
  "user_credentials" : [array of  multiple user credentials]
}
'''
# storing our json file as "data_file" by giving the path
data_file = Path(__file__).parent / "data" / "user_details.json"
# open the file as an object "f"
with open(data_file) as f:
    # we are converting this json sets using load to treat is as a python object, making access to
    # its data
    converting_json_data_into_python_object = json.load(f)
    # printing the json file data in our console
    print(converting_json_data_into_python_object)

    users_data = converting_json_data_into_python_object["user_credentials_from_json_data_file"]


@pytest.mark.parametrize('each_user_credential_fixture', users_data)
# If you go to the conftest.py and check the fixture "browser_setup_and_tear_down_browser",
# it is yield page ( I mean return page)
def test_e2e_web_api_check(playwright: Playwright, browser_setup_and_tear_down_browser, each_user_credential_fixture):
    email = each_user_credential_fixture["user_email"]
    password = each_user_credential_fixture["user_password"]

    creating_order_class_object = APIValidationFirstClass()
    order_id = (creating_order_class_object.create_order_api_validation_rahul_shetty
                (playwright, each_user_credential_fixture))

    # creating an object for login page and this "LoginPage" takes this test's "page" as an argument
    # and sending to its class constructor to perform the desire steps. Now, instead of sending page
    # to the log in class we have sent in argument "browser_setup_and_tear_down_browser".
    # If you notice "browser_setup_and_tear_down_browser" returns "page" [ yield page means return page
    # perform all the actions in test case then come back to the yield to finish the closing scenarios
    # of a test]
    # fixture we return so-called yield the page. So, if we put the fixture name as an argument
    # in the LoginPage Class, it is taking the page that is coming from that fixture, that's what we need.
    # As we are using that page in the fixture to go to url, browser setup, so it is the page that we want
    # to use in our code.
    login_page = LoginPage(browser_setup_and_tear_down_browser)

    # Once we call the login function, it lands into dashboard page, and we create a variable
    # which type is "DashBoard" as we have returned a "dashboard" type object when click the log in
    # check the function "provide_username_password_and_click_log_in" in "LoginPage" Class
    dashboard_page_landing_from_login = (
        login_page.provide_username_password_and_click_log_in(email, password))

    order_history_page = dashboard_page_landing_from_login.click_on_order_button()
    order_details_page = order_history_page.view_the_actual_order_details(order_id)
    order_details_page.verify_the_thank_you_message()

