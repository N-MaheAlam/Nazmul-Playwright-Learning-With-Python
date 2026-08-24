import json
import time
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect

from playwright_basics_pom_into_framework_part_01.page_object_model.dashboard_page_lecture_61_62__2nd_step import Dashboard
from playwright_basics_pom_into_framework_part_01.page_object_model.login_page_lecture_61_1st_step import LoginPage
from playwright_basics_pom_into_framework_part_01.utils.api_utils_lecture_49_50_51_60_important import \
    APIValidationFirstClass

# --------------------- Lecture 48 first building UI Automation for API test ------------------------------
# If we are using "Page" class then the argument will be
# def test_e2e_web_api_check(page: Page):
# But we are using the playwright and opening chrome, page manually. So, use the below format of
# argument

# --------------------- Lecture 58 no hard coding and calling data from json files -------------------

# In our code, there should be no data like username, password, locator's tag name, class name etc.
# what we will do we will create a json file from which we will call the data that we need. Data can be
# stored in json files, Excel files and xml files which we can bring in our test in run time.
# However, json is the popular as software developers creates APIs by which they call something from
# server and display in browser in html format.

# Now, we will create a directory name "data" inside our project file
# "playwright_basics_pom_into_framework_part_01". Then, we will create a json file name
# "user_details.json" on that directory. If you go to the json file you will see how the data are stored,
# mostly in array format in javascript which is also considered as list in python.

# Now, we will call this json file and extract the user credentials and use them according to our need
# see the comments of "path" and json related code lines
# REMEMBER ---- we access json file and convert them using built in utils so that python treats the json
# as list or dictionary
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
# opening the  json file as an object "f"
with open(data_file) as f:
    # we are converting this json sets using load to treat is as a python object, making accessible to
    # its data for our python code
    converting_json_data_into_python_object = json.load(f)
    # printing the json file data in our console
    print(converting_json_data_into_python_object)

    # --------------------- Lecture 59 callings values from json for multiple log in -------------------

    # collecting the login details for the multiple users from the key
    # "user_credentials_from_json_data_file" in "user_details.json" file
    # my target is that no matter how many user details are there, my test will run for
    # each user. If there are 10 users emails and passwords, it will run for 10 times.
    # If you see the "user_details.json" file in a bigger picture It's a dictionary{},
    # which has key "user_credentials_from_json_data_file" and this key has a list[] with multiple
    # values in each index [ { userDetail01 }, {userDetails02}]. Inside the list there is also
    # dictionary with keys "user_email" and "user_password"
    #           [   {"user_email": "nazmul2811@diu.edu.bd",
    #               "user_password": "Rh@r12345512"
    #
    #                  }, {
    #       "user_email": "anshika@gmail.com",
    #       "user_password": "Iamking@000"
    #     }
    # So the hierarchy is like below
    # {Parent dictionary : list[{dictionary01}, {dictionary02} -listened] - Parent dictionaryEnd}

    # Now, in below line, we are just taking the value of key
    # "user_credentials_from_json_data_file". Inside this key, there also list and inside
    # list, there are also dictionary which I already talked about. Storing those credentials in
    # "user_data"
    users_data = converting_json_data_into_python_object["user_credentials_from_json_data_file"]


# This a parameterized fixture details where the name of the parameter is 'each_user_credential_fixture'
# and it's requesting and getting the value from "user_data" by request parameter in fixture
# (login details)
@pytest.mark.parametrize('each_user_credential_fixture', users_data)
# This text has 2 parameter one is playwright as we know already and on is fixture coming from
# "the conftest.py" file. Go and check the 'conftest.py" for more details
def test_e2e_web_api_check(playwright: Playwright, each_user_credential_fixture):
    email = each_user_credential_fixture["user_email"]
    password = each_user_credential_fixture["user_password"]
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    # creating an object for login page and this "LoginPage" takes this test's "page" because
    # we are using this page certainly for our test cases, not any other page. Now, this page is
    # sent as an argument for creating the object and place
    #  it to the constructor of "LoginPage" class so that the methods that we have
    #  in "LoginPage" class can use this "page" into their methods to perform go to, navigate,
    #  and fill etc. these sort with actions.
    login_page = LoginPage(page)

    # calling the "navigate_to_login_page" from "LoginPage" class to navigate to the url
    login_page.navigate_to_login_page()
    login_page.provide_username_password_and_click_log_in(email, password)

    time.sleep(1)

    creating_order_class = APIValidationFirstClass()
    order_id = (creating_order_class.create_order_api_validation_rahul_shetty
                (playwright, each_user_credential_fixture))

    dashboard_page = Dashboard(page)
    dashboard_page.click_on_order_button()

    order_row = page.locator("tr").filter(has_text=order_id)

    order_row.get_by_role("button", name="View").click()

    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")

    order_id_from_ui = page.locator(".col-text.-main").text_content()
    print("Order Id from UI: ", order_id_from_ui)
    page.close()

