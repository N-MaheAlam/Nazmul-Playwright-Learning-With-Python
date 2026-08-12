import time

from playwright.sync_api import Page, expect, Playwright


# ---------------------------- LECTURE 34 ------------------------
def test_with_valid_credential_01(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    page.get_by_label("username").fill("rahulshettyacademy")
    page.get_by_label("password").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    # takes 3 seconds to close the browser
    time.sleep(3)


# ---------------------------- LECTURE 35 ------------------------
def test_with_invalid_credential_02(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    # #id_name from HTML
    page.locator("#username").fill("WrongUserName")
    # --- tagename#id_name.class_name from HTML
    page.locator("input#password.form-control").fill("WrongPassword")
    # here "label" is the value of that particular html tag. this value can be found
    # inside the html tag's "value"
    page.locator("select.form-control").select_option(label="Teacher")
    page.locator("#terms").check()
    page.locator("input#signInBtn").click()
    # expect is an auto wait system that is one of the finest features of playwright where this
    # expect is wait until visible or not visible, not attached, to have text
    expect(page.get_by_text(" username/password.")).to_be_visible()

    time.sleep(2)


# ---------------------------- LECTURE 36 ------------------------
def test_run_in_fire_fox_03(playwright: Playwright):
    # we can skip the new_context() function as we are opening only just one tab
    # but when multiple tabs need to open, we must new_context()
    firefox_browser = playwright.firefox.launch(headless=False).new_context().new_page()
    firefox_browser.goto("https://rahulshettyacademy.com/loginpagePractise/#")
