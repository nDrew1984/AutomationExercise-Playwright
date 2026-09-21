# NOTE: These tests are intentionally order-dependent (Create -> Read -> Update -> Delete),
# relying on module-scoped fixtures (created_account, updated_account, deleted_account)
# that build on each other. They are designed to run together within this file.

import pytest
import requests
import jsonschema
from api_schemas import RESPONSE_CODE_MESSAGE_SCHEMA, READ_ACCOUNT_SCHEMA, UPDATED_ACCOUNT_SCHEMA
from api_endpoints import GET_USER_DETAIL, CREATE_ACCOUNT
from api_test_data import MANDATORY_DATA

# Create Account - status code
@pytest.mark.xfail(reason="API bug: returns HTTP 200 instead of 201")
def test_create_account(created_account):
    response: requests.Response = created_account["response"]
    assert response.status_code == 201

# Negative test - Create Account with existing email
def test_create_account_existing(created_account, session, base_url):
    response = session.post(f"{base_url}{CREATE_ACCOUNT}", data=created_account["account_data"])
    json_data = response.json()

    assert json_data["responseCode"] == 400
    assert json_data["message"] == "Email already exists!"

# Create Account - schema validation
def test_created_account_response_matches_schema(created_account):
    json_data = created_account["response"].json()
    jsonschema.validate(instance=json_data, schema=RESPONSE_CODE_MESSAGE_SCHEMA)

# Create Account - Body response code
def test_created_account_body_response_code(created_account):
    json_data = created_account["response"].json()
    assert json_data["responseCode"] == 201

# Create Account - Success message
def test_created_account_success_message(created_account):
    json_data = created_account["response"].json()
    assert json_data["message"] == "User created!"

# Create Account - Response time is less than 1000 ms
def test_created_account_response_time(created_account):
    response: requests.Response = created_account["response"]
    assert response.elapsed.total_seconds() < 1.0

# Create Account - Content-Type is application/json
@pytest.mark.xfail(reason="API error: Content-Type is text/html")
def test_created_account_content_type(created_account):
    response: requests.Response = created_account["response"]
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# Read Account - HTTP Status code is 200
def test_read_account_status_code(created_account, session, base_url):
    email = created_account["account_data"]["email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})

    assert response.status_code == 200

# Read Account - Schema validation
def test_read_account_schema(created_account, session, base_url):
    email = created_account["account_data"]["email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})
    json_data = response.json()

    jsonschema.validate(instance=json_data, schema=READ_ACCOUNT_SCHEMA)

# Read Account - Body response code
def test_read_account_body_response_code(created_account, session, base_url):
    email = created_account["account_data"]["email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})
    json_data = response.json()

    assert json_data["responseCode"] == 200

# Read Account - Response time is less than 1000 ms
def test_read_account_response_time(created_account, session, base_url):
    email = created_account["account_data"]["email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})

    assert response.elapsed.total_seconds() < 1.0

# Read Account - Data are same as in created Account
def test_read_account_data(created_account, session, base_url):
    account_data = created_account["account_data"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": account_data["email"]})
    user_data = response.json()["user"]

    assert user_data["name"] == account_data["name"]
    assert user_data["email"] == account_data["email"]
    assert user_data["title"] == account_data["title"]
    assert user_data["birth_day"] == account_data["birth_date"]
    assert user_data["birth_month"] == account_data["birth_month"]
    assert user_data["birth_year"] == account_data["birth_year"]
    assert user_data["first_name"] == account_data["firstname"]
    assert user_data["last_name"] == account_data["lastname"]
    assert user_data["company"] == account_data["company"]
    assert user_data["address1"] == account_data["address1"]
    assert user_data["address2"] == account_data["address2"]
    assert user_data["country"] == account_data["country"]
    assert user_data["state"] == account_data["state"]
    assert user_data["city"] == account_data["city"]
    assert user_data["zipcode"] == account_data["zipcode"]

# Update Account - HTTP Status code is 200
def test_update_account_status_code(updated_account):
    response: requests.Response = updated_account["response"]
    assert response.status_code == 200

# Update Account - Response matches JSON schema
def test_update_account_schema(updated_account):
    response: requests.Response = updated_account["response"]
    json_data = response.json()

    jsonschema.validate(instance=json_data, schema=UPDATED_ACCOUNT_SCHEMA)

# Update Account - Body response code is 200
def test_update_account_response_code(updated_account):
    response: requests.Response = updated_account["response"]
    json_data = response.json()    

    assert json_data["responseCode"] == 200

# Update Account - Success message: User updated!
def test_update_account_success_message(updated_account):
    response: requests.Response = updated_account["response"]
    json_data = response.json()    

    assert json_data["message"] == "User updated!"

# Update Account - Response time is less than 1000 ms
def test_update_account_response_time(updated_account):
    response: requests.Response = updated_account["response"]
    assert response.elapsed.total_seconds() < 1.0

# Update Account - Content-Type is application/json
@pytest.mark.xfail(reason="API error: Content-Type is text/html")
def test_update_account_content_type(updated_account):
    response: requests.Response = updated_account["response"]
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# Update Account - Data are same as updated
def test_update_account_data(updated_account, session, base_url):
    update_data = updated_account["update_data"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": update_data["email"]})
    user_data = response.json()["user"]

    assert user_data["name"] == update_data["name"]
    assert user_data["email"] == update_data["email"]
    assert user_data["title"] == update_data["title"]
    assert user_data["birth_day"] == update_data["birth_date"]
    assert user_data["birth_month"] == update_data["birth_month"]
    assert user_data["birth_year"] == update_data["birth_year"]
    assert user_data["first_name"] == update_data["firstname"]
    assert user_data["last_name"] == update_data["lastname"]
    assert user_data["company"] == update_data["company"]
    assert user_data["address1"] == update_data["address1"]
    assert user_data["address2"] == update_data["address2"]
    assert user_data["country"] == update_data["country"]
    assert user_data["state"] == update_data["state"]
    assert user_data["city"] == update_data["city"]
    assert user_data["zipcode"] == update_data["zipcode"]

# Delete Account - HTTP Status code is 200
def test_delete_account_status_code(deleted_account):
    response: requests.Response = deleted_account["response"]
    assert response.status_code == 200

# Delete Account - Response matches JSON schema
def test_delete_account_schema(deleted_account):
    response: requests.Response = deleted_account["response"]
    json_data = response.json()

    jsonschema.validate(instance=json_data, schema=RESPONSE_CODE_MESSAGE_SCHEMA)

# Delete Account - Body status code is 200
def test_delete_account_body_response(deleted_account):
    response: requests.Response = deleted_account["response"]
    json_data = response.json()

    assert json_data["responseCode"] == 200

# Delete Account - Success message: Account deleted!
def test_delete_account_success_message(deleted_account):
    response: requests.Response = deleted_account["response"]
    json_data = response.json()

    assert json_data["message"] == "Account deleted!"    

# Delete Account - Response time is less than 1000 ms
def test_delete_account_response_time(deleted_account):
    response: requests.Response = deleted_account["response"]
    assert response.elapsed.total_seconds() < 1.0

# Delete Account - Content-Type is application/json
@pytest.mark.xfail(reason="API error: Content-Type is text/html")
def test_delete_account_content_type(deleted_account):
    response: requests.Response = deleted_account["response"]
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# Get Deleted Account - HTTP Status code is 404
@pytest.mark.xfail(reason="Status code is 200")
def test_read_deleted_account_status_code(deleted_account, session, base_url):
    email = deleted_account["deleted_email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})

    assert response.status_code == 404

# Get Deleted Account - Response matches JSON schema
def test_read_deleted_account_schema(deleted_account, session, base_url):
    email = deleted_account["deleted_email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})
    json_data = response.json()

    jsonschema.validate(instance=json_data, schema=RESPONSE_CODE_MESSAGE_SCHEMA)

# Get Deleted Account - Body status code is 404
def test_read_deleted_account_body_response_code(deleted_account, session, base_url):
    email = deleted_account["deleted_email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})
    json_data = response.json()

    assert json_data["responseCode"] == 404

# Get Deleted Account - Error message: not found
def test_read_deleted_account_error_message(deleted_account, session, base_url):
    email = deleted_account["deleted_email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})
    json_data = response.json()

    assert "not found" in json_data["message"]

# Get Deleted Account - Response time is less than 1000 ms
def test_read_deleted_account_response_time(deleted_account, session, base_url):
    email = deleted_account["deleted_email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})

    assert response.elapsed.total_seconds() < 1.0

# Get Deleted Account - Content-Type is application/json
@pytest.mark.xfail(reason="API error: Content-Type is text/html")
def test_read_deleted_account_content_type(deleted_account, session, base_url):
    email = deleted_account["deleted_email"]
    response = session.get(f"{base_url}{GET_USER_DETAIL}", params={"email": email})

    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

# Negative test - Create Account with missing mandatory parameter
@pytest.mark.parametrize("missing_field", [
    "name", "email", "password", "firstname", "lastname", 
    "address1", "country", "state", "city", "zipcode", "mobile_number"
    ])
def test_create_account_missing_mandatory_field(session, base_url, missing_field):
    missing_data = MANDATORY_DATA.copy()
    del missing_data[missing_field]

    response = session.post(f"{base_url}{CREATE_ACCOUNT}", data=missing_data)
    json_data = response.json()

    assert json_data["responseCode"] == 400
    assert f"{missing_field} parameter is missing" in json_data["message"]



