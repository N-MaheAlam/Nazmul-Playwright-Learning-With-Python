import json
import time
from pathlib import Path

import pytest
from playwright.sync_api import Playwright, expect

from playwright_basics_pom_into_framework_part_01.utils.api_utils_lecture_49_50_51_60_important import \
    APIValidationFirstClass

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
# and it's getting the value from "user_data" (login details)
@pytest.mark.parametrize('each_user_credential_fixture', users_data)
# This text has 2 parameter one is playwright as we know already and on is fixture coming from
# "the conftest.py" file. Go and check the 'conftest.py" for more details
def test_login_without_credential_using_token_generated_from_api_utils(playwright: Playwright, each_user_credential_fixture):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    # creating an instance of the class from where we will collect the token
    token_from_this_class = APIValidationFirstClass()
    # using object calling the method to get the token of the login credentials that we generated
    # by api calls in function "token_for_login_details" in file placed in "utils" folder name
    # "api_utils_lecture_49_50_51_60_important.py"
    get_token_from_utils_class = token_from_this_class.token_for_login_details(playwright, each_user_credential_fixture)
    # "add_init_script" is used to javascript code in our playwright code. the three apostrophe
    # (""" java code """) is used to define the javascript code. In the script, we are going inside the
    # local storage of our browser and set up the value of token which is nothing but came from
    # the function "token_for_login_details(playwright)" in lecture 49-50-51 file
    page.add_init_script(f"""localStorage.setItem('token','{get_token_from_utils_class}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()

    # expecting the below visible text
    expect(page.locator
           (':text("* If orders Will be more than 7 your last order will get deleted")')).to_be_visible()
    time.sleep(2)
    page.close()


