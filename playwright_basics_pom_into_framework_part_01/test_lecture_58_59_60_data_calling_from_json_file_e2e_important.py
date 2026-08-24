import json
import time
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect

from playwright_basics_pom_into_framework_part_01.page_object_model.login_page_lecture_61_1st_step import LoginPage
from playwright_basics_pom_into_framework_part_01.utils.api_utils_lecture_49_50_51_60_important import \
    APIValidationFirstClass

# --------------------- Lecture 48 first building UI Automation for API test ------------------------------
# If we are using "Page" class then the argument will be
# def test_e2e_web_api_check(page: Page):
# But we are using the playwright and opening chrome, page manually. So, use the below format of
# argument

# --------------------- Lecture 58 no hard coding and calling data from json files -------------------

# In our code there should be no data like username, password, locator's tag name, class name etc.
# what we will do we will create a json file from which we will call the data that we need. Data can be
# stored in json files, Excel files and xml files which we can bring in our test in run time.
# However, json is the popular as software developers creates apis by which they call something from
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
# open the file as an object "f"
with open(data_file) as f:
    # we are converting this json sets using load to treat is as a python object, making accessible to
    # its data
    converting_json_data_into_python_object = json.load(f)
    #  place this line of code for printing the json file data in our console
    print(converting_json_data_into_python_object)

    # --------------------- Lecture 59 callings values from json for multiple log in -------------------

    # collection the login details for the multiple users from the key
    # "user_credentials_from_json_data_file" in "user_details.json" file
    # my target is that no matter how many user details are there, my test will run for
    # each user. If there are 10 users emails and passwords, it will run for 10 times.
    # If you see the "user_details.json" file in a bigger picture It's a dictionary,
    # however, inside dictionary there is a list "user_credentials_from_json_data_file" and this
    # list has indexes are in  dictionary format "{
    #       "user_email": "nazmul2811@diu.edu.bd",  ///////   { key : values }
    #       "user_password": "Rh@r12345512"
    #     }
    # that means the hierarchy is like this list -> dictionary inside - again list inside dictionary

    # Now, in below line, we are just taking the value of key
    # "user_credentials_from_json_data_file". Inside this key, there also dictionary and inside
    # dictionary also list which I already talked about. Storing those credentials in
    # "user_data"
    users_data = converting_json_data_into_python_object["user_credentials_from_json_data_file"]


# This a parameterized fixture details where the name of the parameter is 'each_user_credential_fixture'
# and it's getting the value from "user_data" (login details). I am telling that my method
# "test_e2e_web_api_check" needs a parameter fixture which will extract value from the "user_data".
# That means the data this parameter collects from the "user_data" and store and use it in our
# fixture "each_user_credential_fixture"
@pytest.mark.parametrize('each_user_credential_fixture', users_data)
# This text has 2 parameter one is playwright as we know already and on is fixture coming from
# "the conftest.py" file. Go and check the 'conftest.py" for more details
def test_e2e_web_api_check(playwright: Playwright, each_user_credential_fixture):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    page.goto("https://rahulshettyacademy.com/client")
    #  using the argument "each_user_credential_fixture" we are intercepting the json file
    # "user_details.json" which has a key "user_credentials_from_json_data_file"
    # and from there we are collecting the "user_email" and "user_password"
    page.get_by_placeholder("email@example.com").fill(each_user_credential_fixture["user_email"])
    page.locator("#userPassword").fill(each_user_credential_fixture["user_password"])
    # Till this point from the top of this function is just regular log in info providing
    # and clicking the log in button
    page.get_by_role("button", name="Login").click()
    time.sleep(1)

    # ------------------ LECTURE 52 --  calling the API class to use it in tests --------

    # Creating an object for the "APIValidationFirstClass" which comes from
    # "api_utils_lecture_49_50_51_60_important.py", this file
    creating_order_class = APIValidationFirstClass()

    # ------------------ LECTURE 60 --  modifying utils class method to get data in run time --------
    # Using the object when we call the method "create_order_api_validation_rahul_shetty" and
    # providing 2 arguments one is "playwright" in this function's argument, and
    # another is "each_user_credential_fixture" which is also an argument of this function
    # go and check the "APIValidationFirstClass"
    # It provides the "order_id" that has been collected using API call
    order_id = creating_order_class.create_order_api_validation_rahul_shetty(playwright, each_user_credential_fixture)

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
    # printing the json file that is coming from "user_details.json" located in "data" directory
    print(converting_json_data_into_python_object)
    page.close()
