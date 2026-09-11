import pytest
from test_data import base_url

accept_cookies_button_selector = "button.fc-cta-consent"

# Runs before tests
# navigates to Login page, removes ads and accepts cookies
@pytest.fixture(autouse=True)
def accept_cookies(page):
    page.route("**/*googlesyndication*", lambda route: route.abort())
    page.route("**/*fundingchoicesmessages*", lambda route: route.abort())
    page.route("**/*googleadservices*", lambda route: route.abort())
    page.route("**/*pagead*", lambda route: route.abort())
    page.route("**/*adsbygoogle*", lambda route: route.abort())
  
    page.goto(base_url + "login")
    page.add_locator_handler(
        page.locator(accept_cookies_button_selector), 
        lambda locator: locator.click()
    )
    page.add_locator_handler(
        page.locator("ins.adsbygoogle"),
        lambda locator: locator.evaluate("el => el.remove()")
    )
    yield
