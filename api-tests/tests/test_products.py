import requests
import pytest
import jsonschema
from api_endpoints import PRODUCTS_LIST
from api_schemas import PRODUCTS_LIST_SCHEMA

# Status code is 200
# Response contains products array
# Content-Type header exists
def test_get_product_list(session, base_url):
    response = session.get(f"{base_url}{PRODUCTS_LIST}")
    json_data = response.json()

    assert response.status_code == 200
    assert isinstance(json_data["products"], list)
    assert len(json_data["products"]) > 0
    assert "Content-Type" in response.headers

# Known bug
@pytest.mark.xfail(reason="API error: Content-Type is text/html")
def test_product_list_content_type_is_json(session, base_url):
    response = session.get(f"{base_url}{PRODUCTS_LIST}")

    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# Response time is less than 2000 ms
def test_product_list_response_time(session, base_url):
    response = session.get(f"{base_url}{PRODUCTS_LIST}")

    assert response.elapsed.total_seconds() < 2.0

# Product object has required fields
@pytest.mark.parametrize("field", ["id", "name", "price", "brand"])
def test_product_has_required_field(session, base_url, field):
    response = session.get(f"{base_url}{PRODUCTS_LIST}")
    json_data = response.json()
    first_product = json_data["products"][0]

    assert field in first_product

# Id is a number
def test_product_id_is_number(session, base_url):
    response = session.get(f"{base_url}{PRODUCTS_LIST}")
    json_data = response.json()
    first_product = json_data["products"][0]

    assert isinstance(first_product["id"], int)
    
# Name is a string
def test_product_name_is_string(session, base_url):
    response = session.get(f"{base_url}{PRODUCTS_LIST}")
    json_data = response.json()
    first_product = json_data["products"][0]

    assert isinstance(first_product["name"], str)

# Response matches JSON schema
def test_product_list_matches_schema(session, base_url):
    response = session.get(f"{base_url}{PRODUCTS_LIST}")
    json_data = response.json()

    jsonschema.validate(instance=json_data, schema=PRODUCTS_LIST_SCHEMA)

