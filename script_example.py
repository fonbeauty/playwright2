import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email:").click()
    page.get_by_label("Email:").fill("some@mail.ru")
    page.get_by_label("Email:").press("Tab")
    page.get_by_label("Password:").fill("12345")
    page.get_by_role("button", name="Log in").click()
    expect(page.locator("body")).to_contain_text("Login was unsuccessful. Please correct the errors and try again.")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
