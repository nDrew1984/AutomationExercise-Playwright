from playwright.sync_api import Page
from pages.base_page import BasePage

#selectors, sytax: 'element[attribute="value"]', except id: element = #

class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_name_selector = '#name'
        self.signup_email_selector = '#email'
        self.signup_password_selector = '#password'
        self.signup_first_name_selector = '#first_name'
        self.signup_last_name_selector = '#last_name'
        self.signup_address_selector = '#address1'
        self.signup_country_selector = '#country'
        self.signup_state_selector = '#state'
        self.signup_city_selector = '#city'
        self.signup_zip_code_selector = '#zipcode'
        self.signup_mobile_number_selector = '#mobile_number'
        self.signup_createAccount_button_selector = 'button[data-qa="create-account"]'

    def fill_name(self, name):
        self.page.fill(self.signup_name_selector, name)

    def fill_email(self, email):
        self.page.fill(self.signup_email_selector, email)

    def fill_password(self, password):
        self.page.fill(self.signup_password_selector, password)

    def fill_first_name(self, first_name):
        self.page.fill(self.signup_first_name_selector, first_name)

    def fill_last_name(self, last_name):
        self.page.fill(self.signup_last_name_selector, last_name)

    def fill_address(self, address):
        self.page.fill(self.signup_address_selector, address)

    def select_country(self, country):
        self.page.select_option(self.signup_country_selector, value=country)

    def fill_state(self, state):
        self.page.fill(self.signup_state_selector, state)

    def fill_city(self, city):
        self.page.fill(self.signup_city_selector, city)

    def fill_zip_code(self, zip_code):
        self.page.fill(self.signup_zip_code_selector, zip_code)

    def fill_mobile_number(self, mobile_number):
        self.page.fill(self.signup_mobile_number_selector, mobile_number)

    def click_create_account(self):
        self.page.click(self.signup_createAccount_button_selector)

    def signup(self, password, first_name, last_name, address, country, state, city, zip_code, mobile_number):
        self.fill_password(password)
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.select_country(country)
        self.fill_state(state)
        self.fill_city(city)
        self.fill_zip_code(zip_code)
        self.fill_mobile_number(mobile_number)
        self.click_create_account()

