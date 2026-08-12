import time

import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from playwright_basics_bdd_into_framework_part_02.page_object_model.login_page_lecture_61_1st_step import LoginPage
from playwright_basics_bdd_into_framework_part_02.utils.api_utils_lecture_49_50_51_60_important import \
    APIValidationFirstClass

""""
===================== LECTURE 69 - BASICS BDD DISCUSSION ====================

 BDD = Behaviour Driven Development, Cucumber is a tool that support BDD. 
 Cucumber uses Gherkin as a language which is nothing but plain text with proper key words
 like "When, And, Given, Then, Examples.
 So, the cucumber framework has a "feature" file where we write our feature, scenarios, given, when, then
 and, examples.
 
 This feature file is then connected with a step definition file which is the heart, as this file
 is the place where we implement our code and connect the feature file.
 
 ===================== LECTURE 70 ============================
 Installation:
 From your same folder CLI, write "pip3 install pytest-bdd" or from the 
 project -> settings -> interpreter -> add -> "pytest-bdd"
 
 Now, a feature file can have multiple Scenarios, consider feature as test suites and scenarios as test 
 cases.
 
 Now, go to the "features" directory and write your first feature with extension like "your_name.feature"
 you will see it will be a cucumber format otherwise it will show you to install cucumber and just do 
 that.

 ================================ LECTURE 70 ===========================
  "Feature" we can provide any name and then below it is its description after one tab.
  Scenario = My test name or  the achievement I want from my test
  Scenario Outline = When we have data that we use in features, then we use scenario outline
  Given = it defines my current state, what I have, where I am,
  When = To define the actions such as clicking button, fill with username,
  Then = what is the result, outcome I want after performing the given, then condition
  When we use a variable name inside the feature we use "<variable_name and less than with  symbol

"""

scenarios('features/verify_order_message.feature')
@pytest.fixture
def shareable_data_in_this_module():
    return {}


@given(parsers.parse('place the {username} and {password} in login page from API'))
# the "username and password argument of this method is coming from this above "given" BDD
def grab_order_id_from_ui(playwright, username, password, shareable_data_in_this_module):
    each_user_credential_fixture = {}
    each_user_credential_fixture['user_email'] = username

    each_user_credential_fixture['user_password'] = password
    creating_order_class_object = APIValidationFirstClass()
    # As we know when we call "create_order_api_validation_rahul_shetty" method it asks for
    # two arguments on this one is Playwright type and another is a dictionary type. But when we wrote
    # this current method "grab_order_id_from_ui" we didn't have any arguments. Now, we are giving
    # the playwright argument. But, This a step definition file, and this method will take data from the
    # feature file, not from the json file. [ In the last lecture
    # "test_lecture_63_64_global_browser_fixture_setup_in_conftest_important.py"
    # data came by using parameterization from json file, in BDD it comes from the "feature"'s
    # "Examples" keyword
    # So, to fulfil the method
    # "create_order_api_validation_rahul_shetty" we have defined an emtpy dictionary which is
    # "each_user_credential_fixture = {}" and given them with keys and values

    # each_user_credential_fixture['user_email'] = username
    # and
    # each_user_credential_fixture['user_password'] = password
    # which are nothing but fulfilling our request
    #
    order_id = (creating_order_class_object.create_order_api_validation_rahul_shetty
                (playwright, each_user_credential_fixture))
    # Now, "shareable_data_in_this_module" is a fixture which is empty and I declared in this file.
    # What it is doing that it's returning an empty dictionary and if you notice you will see that the
    # "order_id" variable has life limited into the "grab_order_id_from_ui" method. Once the
    # "order_id" we get by calling the "create_order_api_validation_rahul_shetty" , I am storing that
    # into key "shareable_data_in_this_module['order_id']" with value the updated variable
    # "order_id" pair. Whenever, then this "order_id" I will need, I will simply call from
    # the dictionary "shareable_data_in_this_module" and use in other methods of this step
    # definition file
    shareable_data_in_this_module['order_id'] = order_id


@given('the user in on landing page')
# The "browser_setup_and_tear_down_browser" is coming from the fixture from "conftest.py" file
# Now, "shareable_data_in_this_module" is a fixture which is empty and I declared in this file.
# What it is doing that it's returning an empty dictionary and if you notice you will see that the
# "login_page" variable has life limited into the "user_in_landing_page" method. Once the
# "login_page" is performing its duty such as navigation when it is done, I am storing that
# into key "shareable_data_in_this_module['login_page']" with value the updated variable
# "login_page" pair. Whenever, then this updated login page I will need, I will call from
# the dictionary "shareable_data_in_this_module" and use in other methods of this step
# definition file
def user_in_landing_page(browser_setup_and_tear_down_browser, shareable_data_in_this_module):
    login_page = LoginPage(browser_setup_and_tear_down_browser)
    login_page.navigate_to_login_page()
    shareable_data_in_this_module['login_page'] = login_page

    # Once we call the login function, it lands into dashboard page, and we create a variable
    # which type is "DashBoard" as we have returned a "dashboard" type object when click the log in
    # check the function "provide_username_password_and_click_log_in" in "LoginPage" Class


@when(parsers.parse('I log in with {username} and {password}'))
def login_into_portal(username, password, shareable_data_in_this_module):
    login_page = shareable_data_in_this_module['login_page']
    dashboard_page_landing_from_login = (
        login_page.provide_username_password_and_click_log_in(username, password))
    # We did the same thing  here for dashboard page as "order_id" and "login_page"
    shareable_data_in_this_module['dashboard_page_landing_from_login'] = dashboard_page_landing_from_login

@when('navigate to the order page')
def go_to_the_order_page(shareable_data_in_this_module):
    #
    dashboard_page_landing_from_login = shareable_data_in_this_module['dashboard_page_landing_from_login']
    order_history_page = dashboard_page_landing_from_login.click_on_order_button()
    shareable_data_in_this_module['order_history_page'] = order_history_page

@when('select the order ID')
def select_the_order_ID_from_UI(shareable_data_in_this_module):
    order_id = shareable_data_in_this_module['order_id']
    order_history_page = shareable_data_in_this_module['order_history_page']
    order_details_page = order_history_page.view_the_actual_order_details(order_id)
    shareable_data_in_this_module['order_details_page'] = order_details_page

@then('the order ID should match with API order ID')
def order_IDs_of_both_UI_and_API_should_match(shareable_data_in_this_module):
    order_details_page = shareable_data_in_this_module['order_details_page']
    order_details_page.verify_the_thank_you_message()
    time.sleep(1)
