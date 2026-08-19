from playwright.sync_api import Page
import re

class BasePage:
    def __init__(self, page):
        self.page = page
        self.products_button_selector = 'a[href="/products"]'
        self.cart_button_selector = 'a[href="/view_cart"]'

    def clean_text(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def clean_price_to_int(self, price_text):
        return int(price_text.replace("Rs. ", "").strip())
    
    def click_products_button(self):
        self.page.click(self.products_button_selector)
        self.page.wait_for_url("**/products**")

    def click_cart_button(self):
        self.page.click(self.cart_button_selector)
        self.page.wait_for_url("**/view_cart**")
        

    