from playwright.sync_api import Page
from pages.base_page import BasePage
import random

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.info_product_names = '.productinfo p'
        self.info_prices = '.productinfo h2'
        self.info_add_to_cart_buttons = '.productinfo a.add-to-cart'
        self.overlay_products_names = '.product-overlay p'
        self.overlay_prices = '.product-overlay h2'
        self.overlay_add_to_cart_buttons = '.product-overlay a.add-to-cart'  
        self.continue_shopping = 'button.close-modal'
        
    def add_multiple_to_cart(self, count):
        self.page.wait_for_selector(self.info_add_to_cart_buttons)
        first_buttons = self.page.locator(self.info_add_to_cart_buttons).all()
        total = len(first_buttons)
        actual_count = min(count, total)
        random_samples = random.sample(range(total), actual_count)

        added_products = []

        for i in random_samples:
            first_buttons[i].scroll_into_view_if_needed()
            first_buttons[i].hover()

            product_name = self.page.locator(self.overlay_products_names).nth(i).inner_text()
            added_products.append(product_name)

            self.page.locator(self.overlay_add_to_cart_buttons).nth(i).click()
            try:
                self.page.wait_for_selector(self.continue_shopping)
                self.page.locator(self.continue_shopping).click(timeout=2000)
            except:
                pass

        return added_products

    
            