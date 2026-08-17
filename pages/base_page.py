from playwright.sync_api import Page

# accept_cookies_button_selector = "button.fc-cta-consent"
# Products button selector: <a href="/products" style="color: orange;"><i class="material-icons card_travel" style="font-size: 16px;"></i> Products</a>
# Cart button selector: <a href="/view_cart"><i class="fa fa-shopping-cart"></i> Cart</a>
# selectors, sytax: 'element[attribute="value"]', except id: element = #


class BasePage:
    def __init__(self, page):
        self.page = page
        self.products_button_selector = 'a[href="/products"]'
        self.cart_button_selector = 'a[href="/view_cart"]'

    def click_products_button(self):
        self.page.click(self.products_button_selector)
        self.page.wait_for_url("**/products**")

    def click_cart_button(self):
        self.page.click(self.cart_button_selector)
        self.page.wait_for_url("**/view_cart**")
        

    