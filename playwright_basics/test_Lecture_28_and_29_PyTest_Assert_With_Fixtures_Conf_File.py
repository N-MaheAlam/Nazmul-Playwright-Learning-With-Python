import pytest


@pytest.fixture(scope="module")
def assertion_checking_fixture():
    print("\n\nThis is in module level and return pass and check with the test cases")
    return "pass"


@pytest.fixture(scope="function")
def assertion_checking_fixture_02():
    print(" \n\nThis will run in test level for every test cases ")
    # we use this word yield when we tear down browser, perform something at the end of test
    # the test will follow the above instruction from the feature then will stop when
    # see this word "yield", then the test case performs its duty from its code block. once test's
    # is complete it will come to yield and perform the below instruction
    yield
    print("Execute when each test case execution is finished")


# we can provide multiple fixtures in a test
def test_the_assertion_case_01(assertion_checking_fixture, assertion_checking_fixture_02):
    print("This test will pas because of assertion = pass")
    # change the assert value = "fail" you will see what is expected and actual
    assert assertion_checking_fixture == "pass"


@pytest.mark.nazmul_smoke_test
def test_the_assertion_case_02(assertion_checking_fixture, assertion_checking_fixture_02):
    print(" This is the 2nd test case with assertion")


@pytest.mark.skip
def test_the_assertion_case_03(assertion_checking_fixture, assertion_checking_fixture_02):
    print("This test will be skipped as we used skip annotation")
