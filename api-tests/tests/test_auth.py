import pytest
import requests
import jsonschema
from api_endpoints import VERIFY_LOGIN
from api_schemas import RESPONSE_CODE_MESSAGE_SCHEMA

# Login - HTTP Status code is 200
def test_login_status_code(login_response):
    assert login_response.status_code == 200

# Login - Response matches JSON schema
def test_login_schema(login_response):
    json_data = login_response.json()
    jsonschema.validate(instance=json_data, schema=RESPONSE_CODE_MESSAGE_SCHEMA)
        
# Login - ResponseCode is 200
def test_login_response_code(login_response):
    json_data = login_response.json()
    assert json_data["responseCode"] == 200

# Login - Response message is "User exists!"
def test_login_success_message(login_response):
    json_data = login_response.json()
    assert json_data["message"] == "User exists!"

# Login - Response time is less than 1000 ms
def test_login_response_time(login_response):
    assert login_response.elapsed.total_seconds() < 1.0

# Login - Content-Type is present
def test_login_content_type_exists(login_response):
    assert "Content-Type" in login_response.headers

# Login - Content-Type is application/json
@pytest.mark.xfail(reason="API error: Content-Type is text/html")
def test_login_content_type(login_response):
    assert login_response.headers["Content-Type"] == "application/json; charset=utf-8"

# Login - invalid password, status code
@pytest.mark.xfail(reason="API error: status code is 200")
def test_login_invalid_password_status_code(created_account, session, base_url):
    email = created_account["account_data"]["email"]
    password = "wrong_password"

    response = session.post(f"{base_url}{VERIFY_LOGIN}", data={
        "email": email,
        "password": password
    })

    assert response.status_code == 404  

# Login - invalid password, response content
def test_login_invalid_password_response(created_account, session, base_url):
    email = created_account["account_data"]["email"]
    password = "wrong_password"

    response = session.post(f"{base_url}{VERIFY_LOGIN}", data={
        "email": email,
        "password": password
    })
    json_data = response.json()

    assert json_data["responseCode"] == 404
    assert json_data["message"] == "User not found!"

# Login - invalid email, "email not found" path, status code
@pytest.mark.xfail(reason="API error: status code is 200")
def test_login_invalid_email_status_code(created_account, session, base_url):
    email = "invalid@email.com"
    password = created_account["account_data"]["password"]

    response = session.post(f"{base_url}{VERIFY_LOGIN}", data={
        "email": email,
        "password": password
    })

    assert response.status_code == 404

# Login - invalid email, "email not found" path, response code
def test_login_invalid_email_response_code(created_account, session, base_url):
    email = "invalid@email.com"
    password = created_account["account_data"]["password"]

    response = session.post(f"{base_url}{VERIFY_LOGIN}", data={
        "email": email,
        "password": password
    })
    json_data = response.json()

    assert json_data["responseCode"] == 404

# Login - invalid email, "email not found" path, error message
def test_login_invalid_email_message(created_account, session, base_url):
    email = "invalid@email.com"
    password = created_account["account_data"]["password"]

    response = session.post(f"{base_url}{VERIFY_LOGIN}", data={
        "email": email,
        "password": password
    })
    json_data = response.json()

    assert json_data["message"] == "User not found!"

# Login - missing parameters, status code
@pytest.mark.xfail(reason="API error: status code is 200")
def test_login_missing_parameters_status_code(session, base_url):
    response = session.post(f"{base_url}{VERIFY_LOGIN}")
    assert response.status_code == 400

# Login - missing parameters, response code
def test_login_missing_parameters_response_code(session, base_url):
    response = session.post(f"{base_url}{VERIFY_LOGIN}")
    json_data = response.json()

    assert json_data["responseCode"] == 400

# Login - missing parameters, error message
def test_login_missing_parameters_message(session, base_url):
    response = session.post(f"{base_url}{VERIFY_LOGIN}")
    json_data = response.json()

    assert "email or password parameter is missing" in json_data["message"]

