import re
from playwright.sync_api import Page, expect


def test_login_success(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    # page.get_by_role("link", name="Log in").click()
    page.locator(".ico-login", has_text='Log in').click(timeout=1000)
    page.get_by_label("Email:").click()
    page.get_by_label("Email:").fill("some@mail.ru")
    page.get_by_label("Email:").press("Tab")
    page.get_by_label("Password:").fill("123456")
    page.get_by_role("button", name="Log in").click()

    expect(page.locator("body")).to_contain_text("some@mail.ru")


def test_login_fail(page: Page) -> None:
    page.goto("https://demowebshop.tricentis.com/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email:").click()
    page.get_by_label("Email:").fill("some@mail.ru")
    page.get_by_label("Email:").press("Tab")
    page.get_by_label("Password:").fill("12345")
    page.get_by_role("button", name="Log in").click()

    expect(page.locator("body")).to_contain_text("Login was unsuccessful. Please correct the errors and try again.")
