import pytest


# Here we will define our fixture that we will use frequently in test cases
@pytest.fixture(scope="session")
def run_me_before_everything():
    print("session will be run only once  before initiate_3rd_test")
