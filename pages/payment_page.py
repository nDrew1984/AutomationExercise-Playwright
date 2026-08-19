from pages.base_page import BasePage

# Success Message: "Order Placed!"
# Success url: .../payment_done/3300
# click continue -> base_url

class PaymentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name_on_card = 'input[data-qa="name-on-card"]'
        self.card_number = 'input[data-qa="card-number"]'
        self.cvc = 'input[data-qa="cvc"]'
        self.exp_month = 'input[data-qa="expiry-month"]'
        self.exp_year = 'input[data-qa="expiry-year"]'
        self.pay_and_confirm_order = '#submit'
        self.continue_button = 'a[data-qa="continue-button"]'
        self.success_message = "Order Placed!"

    def fill_name(self, name):
        self.page.fill(self.name_on_card, name)

    def fill_card_number(self, number):
        self.page.fill(self.card_number, number)

    def fill_cvc(self, cvc):
        self.page.fill(self.cvc, cvc)

    def fill_exp_month(self, month):
        self.page.fill(self.exp_month, month)

    def fill_exp_year(self, year):
        self.page.fill(self.exp_year, year)

    def click_confirm(self):
        self.page.click(self.pay_and_confirm_order)

    def payment_process(self, name, card_number, cvc, exp_month, exp_year):
        self.fill_name(name)
        self.fill_card_number(card_number)
        self.fill_cvc(cvc)
        self.fill_exp_month(exp_month)
        self.fill_exp_year(exp_year)
        self.click_confirm()

    def click_continue(self):
        self.page.click(self.continue_button)
    

    