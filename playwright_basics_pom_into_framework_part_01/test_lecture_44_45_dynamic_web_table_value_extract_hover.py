import time

from playwright.sync_api import Page, expect


def test_find_the_price_of_rice_dynamically(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            price_column_value = index
            print(f"Price column value is {price_column_value}")
            break

    price_row_value = page.locator("tr").filter(has_text="Rice")
    expect(price_row_value.locator("td").nth(price_column_value)).to_have_text("37")
    print(f"The actual value of rice inside the table is: "
          f"{price_row_value.locator("td").nth(price_column_value).text_content()}")
    page.close()


def test_mouse_hover_checking_and_click(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    time.sleep(1)
    page.get_by_role("link", name="Reload").click()
    page.close()



