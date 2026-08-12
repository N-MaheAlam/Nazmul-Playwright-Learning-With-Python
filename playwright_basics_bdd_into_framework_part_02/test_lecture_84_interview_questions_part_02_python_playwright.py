# =============== Question 0 ========================
"""


ANSWER:


"""
import pytest

# =============== Question 7 ========================
"""
    What is fixture in pytest?

ANSWER: 
        In pytest, fixtures are nothing but functions that could help us to setup and teardown 
        environment before we run any test. We can also use fixture to use data in our tests.
        Also, we could set the scope of a test by using fixtures scope. 

        1) Reusability - define one and use in multiple test cases 
        2) Automatic setup and tear down - Handles pretest and post-test actions
        3) Scope control - fixtures can run per test, session, class, module
        4) Dependency - Pass fixtures as test argument if test has any dependency 



"""


# Defining this function as a fixture using pytest fixture annotation
@pytest.fixture
def sample_data_use_in_test():
    print("\n\nThis a pre setup code to run the test")
    data = {"name": "Nazmul", "Age": 32}
    # this data will be returned when we call this fixture
    # yield data is like return data. What it is doing, it first executes the statement of this
    # fixture then run the test, once test execution is completed then it comes to the yield
    # statement and run the below code
    yield data
    print("This line is executed after the test execution and comes from fixture at the end of test"
          "execution")


# Before the test is run, it looks for the fixture and run the fixture and according to the fixture
# it gets data as a dictionary
def test_call_the_data_assertion_from_fixture(sample_data_use_in_test):
    # Now, from the "sample_data_use_in_test" fixture it checks whether the name is "Nazmul" or not
    # If correct, then proceed to the next line of code
    assert sample_data_use_in_test["name"] == "Nazmul"
    assert sample_data_use_in_test["Age"] == 32
    print("\nSuccessfully asserted the data from fixture ")
