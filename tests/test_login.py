from playwright.sync_api import Page
from pages.login_page import LoginPage
from test_data import base_url, login_email, login_password
# from page_selectors import login_email_selector, login_password_selector, login_button_selector

# run command: pytest tests/test_login.py -v --headed

def test_login_page_opens(page: Page):
    assert "Login" in page.title()

def test_successful_login(page: Page):
    login_page = LoginPage(page)
    login_page.login(login_email, login_password)
    assert page.url != base_url + "/login"

def test_failed_login(page: Page):
    login_page = LoginPage(page)
    login_page.login("invalid@email.com", "invalidpassword")
    assert page.url == base_url + "/login"
    assert page.get_by_text("Your email or password is incorrect!").is_visible()


