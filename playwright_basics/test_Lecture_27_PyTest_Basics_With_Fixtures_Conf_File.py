import pytest


# We are going to define our fixtures in "conftest.py" file and will use it here.
# if we see that any fixtures that are commonly used in every test cases,
# we can define those fixtures in our "conftest.py" global file and call it
# in every test case placing them in test arguments
# conftest.py is a global file, test cases look for something in local and if they cannot
# find it, then they search in "conftest.py" file.
# file name of the test should also be started with the name "test" see example
# "test_Lecture_27_PyTest_Basics_With_Fixtures_Conf_File.py" and
# "test_Lecture_26_PyTest_Basics_With_Fixtures.py"

# So, when we want  to run a test or a file we can use the run button but if we want to run multiple
# files for example this file ""test_Lecture_27_PyTest_Basics_With_Fixtures_Conf_File.py""
#  and this file "test_Lecture_26_PyTest_Basics_With_Fixtures.py" together, we need to run it from
# terminal from that specific folder path "nazmulmahealam@macbookpro PythonBasics %"
# type "pytest" it will run all the files that name starts with "test"
# if we want to see the output also type " pytest -s" in terminal it will show the output also

# Now, scope can be defined as function, module, class, session based on our test cases need
# function - if the scope is function, it will execute for every test cases
# module - it will run for an entire module for once(module which is not belongs to class).
# for example if there are 5 test cases in a module, it will run only one time for those
# 5 test cases
# class - scope  means the execution of the fixture will be only for that specific class
# session - scope will run only for one time in the whole execution

@pytest.mark.nazmul_smoke_test
def test_initiate_4th(run_me_before_everything):
    print(" This will run after taking instructions from conftest.py file")
