from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from test_data import base_url, login_email, login_password, products_count

def test_prducts_page_opens(page: Page):
    login_page = LoginPage(page)
    base_page = BasePage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()

    assert "Products" in page.title()

def test_checkout_page_opens(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    
    login_page.login(login_email, login_password)
    base_page.click_products_button()

    products_page.add_multiple_to_cart(1)
    base_page.click_cart_button()
    assert "Checkout" in page.title()

    cart_page.delete_all_products()

def test_add_to_cart(page: Page):
    base_page = BasePage(page)
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.login(login_email, login_password)
    base_page.click_products_button()

    products_list = products_page.add_multiple_to_cart(products_count)
    base_page.click_cart_button()

    cart_list = cart_page.get_products_list()
    assert cart_list == products_list
    cart_page.delete_all_products()












    


    