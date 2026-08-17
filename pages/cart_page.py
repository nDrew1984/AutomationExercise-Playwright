from playwright.sync_api import Page
from pages.base_page import BasePage

# Proceed to checkout button selector: <a class="btn btn-default check_out">Proceed To Checkout</a>
# Place order button selector: <a href="/payment" class="btn btn-default check_out">Place Order</a>
# selectors, sytax: 'element[attribute="value"]', except id: element = #
# successful order text: "Order Placed!"

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product_list = '.cart_description h4 a'
        self.delete_buttons = '.cart_delete a'
        self.proceed_to_checkout = 'a[class="btn btn-default check_out"]'
        self.place_order_button = 'a[class="btn btn-default check_out"]'
        self.name_on_card = 'input[data-qa="name-on-card"]'
        self.card_number = 'input[data-qa="card-number"]'
        self.cvc = 'input[data-qa="cvc"]'
        self.expiration_month = 'input[data-qa="expiry-month"]'
        self.expiration_year = 'input[data-qa="expiry-year"]'
        self.confirm_order = '#submit'

    def get_products_list(self):
        self.page.wait_for_selector(self.product_list)
        cart_products = []
        product_locators = self.page.locator(self.product_list).all()
        for product in product_locators:
            name = product.inner_text().strip()
            if name and '\xa0' not in name:
                cart_products.append(name)
        return cart_products

    def click_proceed_to_checkout(self):
        self.page.click(self.proceed_to_checkout)

    def click_place_order(self):
        self.page.click(self.place_order_button)

    def delete_all_products(self):
        while self.page.locator(self.delete_buttons).count() > 0:
            self.page.locator(self.delete_buttons).first.click()
            self.page.wait_for_timeout(500)


    