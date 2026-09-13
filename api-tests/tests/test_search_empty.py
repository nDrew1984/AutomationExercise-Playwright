import requests
import pytest
from api_endpoints import SEARCH_PRODUCT

# HTTP status code is 200
# Response has responseCode and Products
def test_search_empty_string(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}", data={"search_product": ""})
    json_data = response.json()

    assert response.status_code == 200
    assert "responseCode" in json_data
    assert "products" in json_data

# Body response code is 200
# Response contains products
def test_body_content(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}", data={"search_product": ""})
    json_data = response.json()   

    assert json_data["responseCode"] == 200
    assert len(json_data["products"]) > 0

