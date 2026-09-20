import requests
import pytest
import jsonschema
from api_endpoints import PRODUCTS_LIST
from api_schemas import PRODUCTS_LIST_SCHEMA

# Status code is 200
# Response contains products array
# Content-Type header exists
def test_get_product_list(products_response):
    json_data = products_response.json()

    assert products_response.status_code == 200
    assert isinstance(json_data["products"], list)
    assert len(json_data["products"]) > 0
    assert "Content-Type" in products_response.headers

# Known bug
@pytest.mark.xfail(reason="API error: Content-Type is text/html")
def test_product_list_content_type_is_json(products_response):
    assert products_response.headers["Content-Type"] == "application/json; charset=utf-8"

# Response time is less than 2000 ms
def test_product_list_response_time(products_response):
    assert products_response.elapsed.total_seconds() < 2.0

# Product object has required fields
@pytest.mark.parametrize("field", ["id", "name", "price", "brand"])
def test_product_has_required_field(products_response, field):
    json_data = products_response.json()
    first_product = json_data["products"][0]

    assert field in first_product

# Id is a number
def test_product_id_is_number(products_response):
    json_data = products_response.json()
    first_product = json_data["products"][0]

    assert isinstance(first_product["id"], int)
    
# Name is a string
def test_product_name_is_string(products_response):
    json_data = products_response.json()
    first_product = json_data["products"][0]

    assert isinstance(first_product["name"], str)

# Response matches JSON schema
def test_product_list_matches_schema(products_response):
    json_data = products_response.json()

    jsonschema.validate(instance=json_data, schema=PRODUCTS_LIST_SCHEMA)

