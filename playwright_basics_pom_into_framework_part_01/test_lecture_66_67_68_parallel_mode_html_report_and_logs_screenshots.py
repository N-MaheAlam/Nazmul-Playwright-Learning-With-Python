"""
======================== Lecture 66 Parallel Execution ==============================

If we want to run our tests in parallel mode, we need to install a package
 with giving the command in terminal "pip3 install pytest -xdist".
 It will install a package which will help to run the test parallely.
 Now in terminal write in the folder of test terminal
 " pytest -n number_of_threads_to_open_to_run_in_parallel" for example

"pytest -n 5" -> it will open 5 nodes (browsers) to run our test in 5 browsers in the same
 time

======================== Lecture 67 HTML report generate ==============================

In the same way just install in terminal with the command
 " pip3 install pytest-html"
 it will run some files and will install in our machine

Now, we can use the same command as above but need to add html and html report name like below

 "pytest -n 5 --html=it_is_an_html_report.html


======================== Lecture 68 HTML screenshots logs generate ==============================
Link to learn :
 https://playwright.dev/python/docs/trace-viewer-intro

Tracing is used to see each and every step with  screenshots of our tests.
command in terminal of test folder:
 " pytest --tracing on"


Options for tracing are:

 on: Record trace for each test
 off: Do not record trace. (default)
 retain-on-failure: Record trace for each test, but remove all traces from successful test runs.

Let's see the big command line and explain

This line is opening the test firefox as we have already built our own custom key word
 "browser_name" in lecture 63_64, running for each test  which has fixture name by
 "@pytest.mark.smoke", -n 3 is opening 3 browsers (threads) for us to run our tests
  tracing is on means it will generate logs, screenshot for all the test and finally
  generating the html report locating in project level"
 "pytest --browser_name firefox -m smoke -n 3 --tracing on --html=report_name_in_project_level.html"

So, once we run the command, we will see a folder name with "test-results" has been generated.
 Inside the folder we can see the traces for each test file. However, it is showing for 13 test because
 some of the test we make them "headless = False" that means open browser that's why.

Now, go to "trace.playwright.dev" link and upload the "trace.zip" file from the "test-results"
 folder. Each test has its own "trace.zip" file and upload on that website. You then can see the
 logs, screenshots, step by step so that we can deep dive and debug and find out where is the
 actual problem

"""