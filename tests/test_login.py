from playwright.sync_api import Page
from test_data import base_url, login_email, login_password
from page_selectors import login_email_selector, login_password_selector, login_button_selector

# run command: pytest tests/test_login.py -v --headed

def test_login_page_opens(page: Page):
    assert "Login" in page.title()

def test_successful_login(page: Page):
    page.fill(login_email_selector, login_email)
    page.fill(login_password_selector, login_password)
    page.click(login_button_selector)
    assert page.url != base_url + "/login"

def test_failed_login(page: Page):
    page.fill(login_email_selector, "invalid@email.com")
    page.fill(login_password_selector, "invalidpassword")
    page.click(login_button_selector)
    assert page.url == base_url + "/login"
    assert page.get_by_text("Your email or password is incorrect!").is_visible()



