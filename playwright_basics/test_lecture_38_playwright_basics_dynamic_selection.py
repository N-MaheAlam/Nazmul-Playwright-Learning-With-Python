import time

from playwright.sync_api import Page, Playwright, expect


def test_add_to_cart_item(playwright: Playwright):
    fire_fox_browser = playwright.firefox.launch(headless=False).new_context().new_page()
    fire_fox_browser.goto("https://rahulshettyacademy.com/loginpagePractise/#")
    fire_fox_browser.get_by_label("Username:").fill("rahulshettyacademy")
    fire_fox_browser.get_by_label("Password:").fill("Learning@830$3mK2")
    fire_fox_browser.get_by_role("combobox").select_option("teach")
    fire_fox_browser.locator("#terms").check()
    fire_fox_browser.get_by_role("button", name="Sign In").click()
    # app-card is a tagName, if it was a class or id we would use # or .
    i_phone = fire_fox_browser.locator("app-card").filter(has_text="iphone X")
    i_phone.get_by_role("button").click()
    back_berry = fire_fox_browser.locator("app-card").filter(has_text="Blackberry")
    back_berry.get_by_role("button").click()
    fire_fox_browser.get_by_text("Checkout").click()

    expect(fire_fox_browser.locator(".media-body")).to_have_count(2)

    time.sleep(2)
