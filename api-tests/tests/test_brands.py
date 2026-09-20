import requests
import pytest
import jsonschema
from api_endpoints import BRANDS_LIST
from api_schemas import BRANDS_LIST_SCHEMA

# Status code is 200
# Response contains Brands array
# Content-Type header exists
def test_brand_list(brands_response):
    json_data = brands_response.json()

    assert brands_response.status_code == 200
    assert isinstance(json_data["brands"], list)
    assert len(json_data["brands"]) > 0
    assert "Content-Type" in brands_response.headers

# Content-Type is application/json
# Known bug
@pytest.mark.xfail(reason="API error: Content-Type is text/html")
def test_brand_list_content_type_is_json(brands_response):
    assert brands_response.headers["Content-Type"] == "application/json; charset=utf-8"

# Response time is less than 2000ms
def test_brand_list_response_time(brands_response):
    assert brands_response.elapsed.total_seconds() < 2.0

# Brand object has required fields
@pytest.mark.parametrize("field", ["id", "brand"])
def test_brand_has_required_fields(brands_response, field):
    json_data = brands_response.json()
    first_brand = json_data["brands"][0]

    assert field in first_brand

# Id is a number
def test_brand_id_is_number(brands_response):
    json_data = brands_response.json()
    first_brand = json_data["brands"][0]

    assert isinstance(first_brand["id"], int)

# Brand is a string
def test_brand_is_string(brands_response):
    json_data = brands_response.json()
    first_brand = json_data["brands"][0]

    assert isinstance(first_brand["brand"], str)

# Response matches JSON schema
def test_brands_list_matches_schema(brands_response):
    json_data = brands_response.json()

    jsonschema.validate(instance=json_data, schema=BRANDS_LIST_SCHEMA)
