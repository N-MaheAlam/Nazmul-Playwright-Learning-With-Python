import time

from playwright.sync_api import Page


# ---------------------- LECTURE 39 -Child Window Handle --------------------

def test_child_window_handle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    # click this link which will open a new child window

    # I am telling to my code that any new window might pop up and capture it as a new_child_page_info
    with page.expect_popup() as new_child_page_info:
        # Once we click the link it will open a new child window
        page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material"
                         ).click()
        # this "child_page" is capturing "new_child_page_info.value" so that we can perform our task
        # in child window such as click, check, text collecting. In addition, we can use parents object
        #  "page" inside this child block to navigate to parent window. Only when we want to do tests
        # in child window, we will use "child_page.playwright_function_name" to perform our
        # requirements
        child_page = new_child_page_info.value

        text = child_page.locator(".im-para.red").text_content()
        # Printing the whole text on the console
        # ---------------------- LECTURE 40 - Splitting text from UI --------------------
        print(text)
        # the whole sentence " Please email us at mentor@rahulshettyacademy.com with below
        # template to receive response " split using "at". So it is a list now of 2 indexes
        # [' Please email us',' mentor@rahulshettyacademy.com with below  template to receive response ']
        # there is no "at" in the indexes of the list as we are splitting using "at"
        # Now, we went to index[1] which is ' mentor@rahulshettyacademy.com with below
        # template to receive response ' then removes the space from left and right side using
        # "strip()', then split when it's found space [space after the email]. Now have a new list
        # ['mentor@rahulshettyacademy.com','with below  template to receive response']
        # now it collects the 0 index which is "mentor@rahulshettyacademy.com"
        email_address = text.split("at")[1].strip().split(" ")[0]
        print(email_address)
        # checking the email that we got from the website is same as the requirement
        assert email_address == "mentor@rahulshettyacademy.com"

