import pytest


# this "pytest.fixture" is used to run any code before we run our test cases
# This helps to run like opening browsers, some initial data for all test cases,
# for log in to perform some specific test cases
# In "scope" if we put "function" this will be run for every test cases,
# If we put "module" it will be run for one time and will perform all the test cases
# "scope" can be module, function, class, session
# we use class as scope when we have some codes inside a class, and we want to run  this class only

@pytest.fixture(scope="module")
def initial_this_code_before():
    print(" I will be initialized first before I run tests")


# In pytest, "test_function_name" is treated as a test because the name we start
# with "test________" so that pytest understand it's a test.
# In argument, we give fixtures  and here,
# giving "initial_this_code_before" means before running this test
# it will run "initial_this_code_before" first to initiate for example browsers,
def test_initial_first_check(initial_this_code_before):
    print(" This is the 1st test, can be run by the green button or selecting manually")


def test_initial_second_check(initial_this_code_before):
    print(" This is the 2nd test cases ")


def test_initial_third_check(run_me_before_everything):
    print(" This is the 3rd test cases ")
