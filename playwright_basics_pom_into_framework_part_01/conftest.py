import time

import pytest


# here "request" is a built-in parameter or argument whatever you say, it has the power to access
# global variables as well as the local functions variables parameters
# this fixture is requesting for a parameter. When we will use this fixture, we need to provide a
# parameter with name and beside that the variable name from which it will request data
@pytest.fixture(scope="session")
def each_user_credential_fixture(request):
    # by this request.param it will access to local variables such as variables present in tests.
    # json files.
    return request.param


# ---------------------------- LECTURE 63, 64 how to set up variable in command line
# ------------------------

# this "pytest_addoption" will set a variable that we can modify
# on command line prompt, name "browser_name" that we can use in CLI.
# in its parameter it's saying my command line variable will be "browser_name"
# the "action" keyword is representing what we are doing with this keyword.
# We are storing such as the "--browser_name" to use it right? So, it
# will be storing that value to use according to the command
# if no value is given to for example if we do not provide which browser it should run then,
# where it should run? That's why we are giving the default value will be "chrome" means if we
# do not give any browser name it should run on chrome. "help" keyword is used to give definition
# for that specific keyword. "help" is just additional comment you can declare on that.
# This is a built-in function of pytest.
# Now, with the "parser.addoption" we can add multiple global CLI variables, all we need to do, change
# the name, action, default and help values
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Type of browser: chrome or firefox"
    )
    # setting another command line variable which is "url_name". action is stores, if now url is given
    # then default will be "https://rahulshettyacademy.com/client"
    parser.addoption(
        "--url_name",
        action="store",
        default="https://rahulshettyacademy.com/client",
        help="server selection"
    )


#                                   LECTURE -64

# Here, we haven't used scope = session, because, We are running our code by using 2 data sets from
# the json file. So, if we give scope = session what it will do, after loging in with the first data
# sets (username and password) it will perform its actions such as navigate, click, scroll and
# when the test is finished for first data sets, it will return the page which has already the log in
# token details of first data sets. Finally, when the test will be run for 2nd data sets it will
# directly land on dashboard page instead of log in page which will lead to error.
@pytest.fixture
def browser_setup_and_tear_down_browser(playwright, request):
    #  we are storing the "--browser_name" from terminal in "browser_name" variable, not the parameter
    # one (--browser_name)
    browser_name = request.config.getoption("--browser_name")
    # setting another global variable url_name which will come from the command line and will use when
    # any test has this fixture. That means, when we call the test which has this fixture
    # from command line, the test can set its url_name from the command line. Same for the above
    # "browser_name"
    url_name = request.config.getoption("--url_name")

    # In terminal if the browser name is given as chrome, then launch the Chrome browser
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    ## In terminal if the browser name is given as firefox, then launch the firefox browser
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError("Unsupported browser")

    context = browser.new_context()
    page = context.new_page()
    page.goto(url_name)
    #  "yield page" means you can say one kind of "return page"
    yield page
    print("\nThis statement comes from fixture because of yield and after every text execution"
          ", Execution is successfully completed :) \n\n ================= TEST ENDS ===============")
    context.close()
    time.sleep(1)
