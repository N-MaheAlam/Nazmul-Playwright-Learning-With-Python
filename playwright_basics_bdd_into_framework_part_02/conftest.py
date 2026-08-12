import pytest


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
# the "action" will be storing that value to use according to the command
# if no value is given the default value will be "chrome"
# "help" is just additional comment you can declare on that. This is a built in function of pytest
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
