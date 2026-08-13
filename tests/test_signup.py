from playwright.sync_api import Page
from test_data import signup_name, signup_email, signup_password, signup_first_name, signup_last_name, signup_address, signup_Country, signup_state, signup_city, signup_zip_code, signup_mobile_number
from page_selectors import name_selector, email_address_selector, signup_button_selector, signup_name_selector, signup_email_selector, signup_password_selector, signup_first_name_selector, signup_last_name_selector, signup_address_selector, signup_country_selector, signup_state_selector, signup_city_selector, signup_zip_code_selector, signup_mobile_number_selector, signup_createAccount_button_selector, login_email_selector, login_password_selector, login_button_selector

#run command: pytest tests/test_signup.py -v --headed

# Testing page title
def test_signup_page_opens(page: Page):
    page.fill(name_selector, signup_name)
    page.fill(email_address_selector, signup_email)
    page.click(signup_button_selector)

    assert "Signup" in page.title()

# Testing name and email fields are prefilled
def test_fields_prefilled(page: Page):
    page.fill(name_selector, signup_name)
    page.fill(email_address_selector, signup_email)
    page.click(signup_button_selector)

    filled_name = page.input_value(signup_name_selector)
    filled_email = page.input_value(signup_email_selector)

    assert filled_name == signup_name
    assert filled_email == signup_email

# Testing successful signup
def test_successful_signup(page: Page):
    page.fill(name_selector, signup_name)
    page.fill(email_address_selector, signup_email)
    page.click(signup_button_selector)

    page.fill(signup_password_selector, signup_password)
    page.fill(signup_first_name_selector, signup_first_name)
    page.fill(signup_last_name_selector, signup_last_name)
    page.fill(signup_address_selector, signup_address)
    page.select_option(signup_country_selector, value=signup_Country)
    page.fill(signup_state_selector, signup_state)
    page.fill(signup_city_selector, signup_city)
    page.fill(signup_zip_code_selector, signup_zip_code)
    page.fill(signup_mobile_number_selector, signup_mobile_number)

    page.click(signup_createAccount_button_selector)

    assert "Account Created" in page.title()

# Testing login with newly created account
def test_login_with_new_account(page: Page):
    page.fill(login_email_selector, signup_email)
    page.fill(login_password_selector, signup_password)
    page.click(login_button_selector)

    assert page.get_by_text("Logged in as " + signup_name).is_visible()
