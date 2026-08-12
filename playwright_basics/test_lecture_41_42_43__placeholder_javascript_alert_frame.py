import time

from playwright.sync_api import Page, expect, sync_playwright


# ---------------------- LECTURE 41 - placeholder - visible - invisible -----------------
def test_placeholder_use_visible_invisible(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    expect(page.get_by_placeholder("Hide/Show Example")).not_to_be_visible()
    time.sleep(1)


# ---------------------- LECTURE 42 Javascript Alert Handle -----------------
def test_pop_up_alerts(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # This code is used to handle the javascript pop windows which playwright does not have
    # access. Call it by "page.on" then the 2 arguments one will be "dialog and other will be function
    # "lambda" is used for anonymous function that does not need any name as we will just call it on
    # that particular code only. We are alerting that pop up can be triggered before we click the button
    # so our test is alert and once we click it grabs the pop-up and follow the instructions. It's like
    # telling security guard " please watch the door if anyone is outside or not. Security is alert, and you
    # tell him to proceed to open the door". If I put click() first, its like I opened the door
    # without checking outside and telling the security to let me inform which is a security risk right?.

    page.on("dialog", lambda dialog: dialog.accept())
    page.locator("#confirmbtn").click()
    time.sleep(2)


# ---------------------- LECTURE 43 Frame Handling -----------------

def test_frame_handling(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # frame is nothing but a html page embedded in parent html page. To perform our task on
    # a fram we use "frame.locator" to do , click, fill, any locators activity
    frame_page = page.frame_locator("#courses-iframe")
    frame_page.get_by_role("link", name="All Access plan").click()
    expect(frame_page.locator("body")).to_contain_text("Happy Subscibers")


# This test is to run in iPhone 13
def test_mobile():
    with sync_playwright() as p:
        iphone = p.devices["iPhone 13"]

        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**iphone)
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/AutomationPractice/")

        # This code is used to handle the javascript pop windows which playwright does not have
        # access. Call it by "page.on" then the 2 arguments one will be "dialog and other will be function
        # "lambda" is used for anonymous function that does not need any name as we will just call it on
        # that particular code only. We are alerting that pop up can be triggered before we click the button
        # so our test is alert and once we click it grabs the pop-up and follow the instructions. It's like
        # telling security guard " please watch the door if anyone is outside or not. Security is alert, and you
        # tell him to proceed to open the door". If I put click() first, its like I opened the door
        # without checking outside and telling the security to let me inform which is a security risk right?.

        page.on("dialog", lambda dialog: dialog.accept())
        page.locator("#confirmbtn").click()
        time.sleep(2)
