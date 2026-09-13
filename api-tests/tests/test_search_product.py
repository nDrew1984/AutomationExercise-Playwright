import requests
import pytest
import jsonschema
from api_endpoints import SEARCH_PRODUCT
from api_schemas import PRODUCTS_LIST_SCHEMA
from api_test_data import SEARCH_TERM_VALID

# HTTP status code is 200
# Response contains at least one result
# Body response code is 200
def test_search_product_valid(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}", data={"search_product": SEARCH_TERM_VALID})
    json_data = response.json()

    assert response.status_code == 200
    assert len(json_data["products"]) > 0
    assert json_data["responseCode"] == 200

# Response matches JSON schema
def test_response_matches_schema(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}", data={"search_product": SEARCH_TERM_VALID})
    json_data = response.json()

    jsonschema.validate(instance=json_data, schema=PRODUCTS_LIST_SCHEMA)

# Body contains the searched string
# Every product contains the searched string
def test_body_contains_searched_term(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}", data={"search_product": SEARCH_TERM_VALID})

    assert SEARCH_TERM_VALID.lower() in response.text.lower()

    json_data = response.json()
    products = json_data["products"]

    for product in products:
        matches_name = SEARCH_TERM_VALID.lower() in product["name"].lower()
        matches_usertype = SEARCH_TERM_VALID.lower() in product["category"]["usertype"]["usertype"].lower()
        matches_category = SEARCH_TERM_VALID.lower() in product["category"]["category"].lower()

        assert matches_name or matches_usertype or matches_category

        
