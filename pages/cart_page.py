from playwright.sync_api import Page
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_rows = 'tbody tr'
        self.product_names = '.cart_description h4 a'
        self.product_prices = '.cart_price p'
        self.product_quantities = '.cart_quantity button'
        self.product_totals = '.cart_total p'
        self.delete_buttons = '.cart_delete a'
        self.proceed_to_checkout = 'a[class="btn btn-default check_out"]'
        self.place_order_button = 'a[class="btn btn-default check_out"]'
        self.name_on_card = 'input[data-qa="name-on-card"]'
        self.card_number = 'input[data-qa="card-number"]'
        self.cvc = 'input[data-qa="cvc"]'
        self.expiration_month = 'input[data-qa="expiry-month"]'
        self.expiration_year = 'input[data-qa="expiry-year"]'
        self.confirm_order = '#submit'
        self.empty_cart_message = "Cart is empty!"

    def get_products_list(self):
        self.page.wait_for_selector(self.product_names)
        cart_products = []
        product_locators = self.page.locator(self.product_names).all()
        for product in product_locators:
            name = self.clean_text(product.inner_text())
            cart_products.append(name)
        return cart_products

    def get_cart_details(self):
        self.page.wait_for_selector(self.product_rows)
        cart_items = []
        rows = self.page.locator(self.product_rows).all()
        for row in rows:
            if row.locator(self.product_names).count() > 0:
                item = {
                    "name": row.locator(self.product_names).inner_text(),
                    "price": self.clean_price_to_int(row.locator(self.product_prices).inner_text()),
                    "quantity": int(row.locator(self.product_quantities).inner_text().strip()),
                    "total": self.clean_price_to_int(row.locator(self.product_totals).inner_text())
                }
                cart_items.append(item)
        return cart_items

    def get_total_amount(self):
        text = self.page.locator('tr', has=self.page.get_by_text("Total Amount")).locator('.cart_total_price').inner_text()
        return self.clean_price_to_int(text)

    def click_proceed_to_checkout(self):
        self.page.click(self.proceed_to_checkout)
        self.page.wait_for_url("**/checkout**")

    def click_place_order(self):
        self.page.click(self.place_order_button)
        self.page.wait_for_url("**/payment**")

    def delete_all_products(self):
        while self.page.locator(self.delete_buttons).count() > 0:
            self.page.locator(self.delete_buttons).first.click()
            self.page.wait_for_timeout(500)


    