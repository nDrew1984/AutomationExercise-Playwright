import requests
import pytest
from api_endpoints import SEARCH_PRODUCT

# HTTP status code is 400
@pytest.mark.xfail(reason="API bug: returns HTTP 200 instead of 400 when search_product parameter is missing")
def test_search_without_parameter(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}")
    assert response.status_code == 400

# Body response code is 400
# Error message mentions missing parameter
def test_body_resoponse_code_and_error_message(session, base_url):
    response = session.post(f"{base_url}{SEARCH_PRODUCT}")
    json_data = response.json()
    expected_text = "parameter is missing"

    assert json_data["responseCode"] == 400
    assert expected_text in json_data["message"]

