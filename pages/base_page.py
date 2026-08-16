from playwright.sync_api import Page

# accept_cookies_button_selector = "button.fc-cta-consent"

class BasePage:
    def __init__(self, page):
        self.page = page

    # def accept_cookies(self):
    #     try:
    #         self.page.locator(accept_cookies_button_selector).click(timeout=3000)
    #     except:
    #         pass

    # def navigate(self, url):
    #     self.page.goto(url)
    #     self.accept_cookies()
    #     self.page.wait_for_load_state("networkidle")

    