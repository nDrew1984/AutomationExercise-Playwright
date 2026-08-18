from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_email_selector = 'input[data-qa="login-email"]'
        self.login_password_selector = 'input[data-qa="login-password"]'
        self.login_button_selector = 'button[data-qa="login-button"]'
        self.signup_name_selector = 'input[data-qa="signup-name"]'
        self.signup_email_selector = 'input[data-qa="signup-email"]'
        self.signup_button_selector = 'button[data-qa="signup-button"]'

    def fill_email(self, email):
        self.page.fill(self.login_email_selector, email)

    def fill_login_password(self, password):
        self.page.fill(self.login_password_selector, password)

    def fill_signup_name(self, name):
        self.page.fill(self.signup_name_selector, name)

    def fill_signup_email(self, email):
        self.page.fill(self.signup_email_selector, email)    

    def click_login(self):
        self.page.click(self.login_button_selector)

    def click_signup(self):
        self.page.click(self.signup_button_selector)

    def login(self, email, password):
        self.fill_email(email)
        self.fill_login_password(password)
        self.click_login()

    def start_Signup(self, name, email):
        self.fill_signup_name(name)
        self.fill_signup_email(email)
        self.click_signup()