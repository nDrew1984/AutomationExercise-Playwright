from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from test_data import signup_name, signup_email, signup_password, signup_first_name, signup_last_name, signup_address, signup_Country, signup_state, signup_city, signup_zip_code, signup_mobile_number

# Testing page title
def test_signup_page_opens(page: Page):
    login_page = LoginPage(page)
    login_page.start_Signup(signup_name, signup_email)
    assert "Signup" in page.title()

# Testing name and email fields are prefilled
def test_fields_prefilled(page: Page):
    login_page = LoginPage(page)
    signup_page = SignupPage(page)
    login_page.start_Signup(signup_name, signup_email)
    
    filled_name = signup_page.page.input_value(signup_page.signup_name_selector)
    filled_email = signup_page.page.input_value(signup_page.signup_email_selector)

    assert filled_name == signup_name
    assert filled_email == signup_email

# Testing successful signup
def test_successful_signup(page: Page):
    login_page = LoginPage(page)
    signup_page = SignupPage(page)

    login_page.start_Signup(signup_name, signup_email)
    signup_page.signup(signup_password, signup_first_name, signup_last_name, signup_address, signup_Country, signup_state, signup_city, signup_zip_code, signup_mobile_number)

    assert "Account Created" in page.title()

# Testing login with newly created account
def test_login_with_new_account(page: Page):
    login_page = LoginPage(page)
    login_page.login(signup_email, signup_password)

    assert page.get_by_text("Logged in as " + signup_name).is_visible()
