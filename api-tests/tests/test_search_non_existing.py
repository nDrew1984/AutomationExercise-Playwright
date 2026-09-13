import requests
import pytest
from api_endpoints import SEARCH_PRODUCT
from api_test_data import SEARCH_TERM_NON_EXISTING

# HTTP status code is 200
# Response has responseCode and Products
def test_search_non_existing(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}", data={"search_product": SEARCH_TERM_NON_EXISTING})
    json_data = response.json()

    assert response.status_code == 200
    assert "responseCode" in json_data
    assert "products" in json_data

# Response does not contain products
# Body response code is 200
def test_body_content(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}", data={"search_product": SEARCH_TERM_NON_EXISTING})
    json_data = response.json()   

    assert json_data["responseCode"] == 200
    assert json_data["products"] == [] 

