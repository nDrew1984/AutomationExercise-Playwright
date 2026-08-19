from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.payment_page import PaymentPage
from test_data import base_url, login_email, login_password, products_count, name_on_card, card_number, cvc, expiration_month, expiration_year

# Testing product page opens successfully
def test_products_page_opens(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()

    assert "Products" in page.title()

# Testing cart page opens successfully
def test_cart_page_opens(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    
    login_page.login(login_email, login_password)
    base_page.click_products_button()

    products_page.add_multiple_to_cart(1)
    base_page.click_cart_button()
    try:
        assert page.url == base_url + "view_cart"
    finally:
        cart_page.delete_all_products()

# Add products to cart, and checking if they appear on the Cart page
def test_add_to_cart(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()

    products_data = products_page.add_multiple_to_cart(products_count)
    product_names = [item["name"] for item in products_data]
    base_page.click_cart_button()

    cart_list = cart_page.get_products_list()
    try:
        assert cart_list == product_names
    finally:
        cart_page.delete_all_products()

# Testing unit prices in Cart page
def test_cart_page_prices(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()

    products_data = products_page.add_multiple_to_cart(products_count)
    base_page.click_cart_button()
    cart_details = cart_page.get_cart_details()
    cart_prices = [{"name": item["name"], "price": item["price"]} for item in cart_details]
    try:
        assert products_data == cart_prices
    finally:
        cart_page.delete_all_products()

# Testing total prices in Cart page (total = unit price * quantity)
def test_totals_cart(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()
    products_page.add_multiple_to_cart(products_count)
    base_page.click_cart_button()

    cart_items = cart_page.get_cart_details()
    try:
        for item in cart_items:
            assert item["total"] == item["price"] * item["quantity"]
    finally:
        cart_page.delete_all_products()
     
# Testing checkout page opens successfully
def test_checkout_page_opens(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()

    products_page.add_multiple_to_cart(1)
    base_page.click_cart_button()
    cart_page.click_proceed_to_checkout()
    try:
        assert page.url == base_url + "checkout"
    finally:
        base_page.click_cart_button()
        cart_page.delete_all_products()

# Testing Checkout table = Cart table
def test_checkout_data(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()
    products_page.add_multiple_to_cart(products_count)
    base_page.click_cart_button()

    cart_details = cart_page.get_cart_details()
    cart_page.click_proceed_to_checkout()
    checkout_details = cart_page.get_cart_details()
    try:
        assert cart_details == checkout_details
    finally:
        base_page.click_cart_button()
        cart_page.delete_all_products()

# Testing Total Amount in Checkout page
def test_total_amount(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()
    products_page.add_multiple_to_cart(products_count)
    base_page.click_cart_button()
    cart_page.click_proceed_to_checkout()

    cart_details = cart_page.get_cart_details()
    totals = [item["total"] for item in cart_details]
    total_amount = cart_page.get_total_amount()
    try:
        assert total_amount == sum(totals)
    finally:
        base_page.click_cart_button()
        cart_page.delete_all_products()

# Testing Payment page opens successfully
def test_payment_page_opens(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()
    products_page.add_multiple_to_cart(1)
    base_page.click_cart_button()
    cart_page.click_proceed_to_checkout()
    cart_page.click_place_order()
    try:
        assert "Payment" in page.title()
    finally:
        base_page.click_cart_button()
        cart_page.delete_all_products()

# Testing Payment process
def test_payment_process(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    payment_page = PaymentPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()
    products_page.add_multiple_to_cart(1)
    base_page.click_cart_button()
    cart_page.click_proceed_to_checkout()
    cart_page.click_place_order()

    payment_page.payment_process(name_on_card, card_number, cvc, expiration_month, expiration_year)

    assert page.get_by_text(payment_page.success_message).is_visible()
    assert "payment_done" in page.url

# Testing url after payment, and empty cart
def test_cart_after_payment(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    payment_page = PaymentPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()
    products_page.add_multiple_to_cart(1)
    base_page.click_cart_button()
    cart_page.click_proceed_to_checkout()
    cart_page.click_place_order()
    payment_page.payment_process(name_on_card, card_number, cvc, expiration_month, expiration_year)   

    payment_page.click_continue()
    assert page.url == base_url

    base_page.click_cart_button()
    assert page.get_by_text(cart_page.empty_cart_message).is_visible()

    