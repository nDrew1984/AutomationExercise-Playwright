import pytest
from test_data import base_url

# Cookie accept button: 
# <button class="fc-button fc-cta-consent fc-primary-button" role="button" aria-label="Beleegyezés" 
# tabindex="0"><div class="fc-button-background"></div><p class="fc-button-label">Beleegyezés</p></button>

accept_cookies_button_selector = "button.fc-cta-consent"

@pytest.fixture(autouse=True)
def accept_cookies(page):
    page.goto(base_url + "/login")
    page.add_locator_handler(
        page.locator(accept_cookies_button_selector), 
        lambda locator: locator.click()
    )
    yield
