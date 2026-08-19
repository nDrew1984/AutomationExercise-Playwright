from playwright.sync_api import Page
from pages.base_page import BasePage
import random

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.single_products = '.single-products'
        self.info_product_names = '.productinfo p'
        self.info_prices = '.productinfo h2'
        self.info_add_to_cart_buttons = '.productinfo a.add-to-cart'
        self.overlay_products_names = '.product-overlay p'
        self.overlay_prices = '.product-overlay h2'
        self.overlay_add_to_cart_buttons = '.product-overlay a.add-to-cart'  
        self.continue_shopping = 'button.close-modal'

    # Note: clicking info add-to-cart buttons instead of overlay buttons
    # for stability reasons (ads interfere with hover actions)
    # Both buttons trigger the same cart functionality
    def add_multiple_to_cart(self, count):
        self.page.wait_for_selector(self.info_add_to_cart_buttons)
        info_add_to_cart_buttons = self.page.locator(self.info_add_to_cart_buttons).all()
        total = len(info_add_to_cart_buttons)
        actual_count = min(count, total)
        random_samples = random.sample(range(total), actual_count)

        added_products = []

        for i in random_samples:
            product_name = self.page.locator(self.info_product_names).nth(i).inner_text()
            product_price = self.clean_price_to_int(self.page.locator(self.info_prices).nth(i).inner_text())
            self.page.locator(self.info_add_to_cart_buttons).nth(i).click()

            self.page.wait_for_selector(self.continue_shopping)
            #self.page.locator(self.continue_shopping).click(timeout=2000)
            self.page.locator(self.continue_shopping).click()

            added_products.append({
                "name": product_name,
                "price": product_price
            })
        return added_products

    
            