import pytest
import requests
from api_endpoints import PRODUCTS_LIST, BRANDS_LIST, CREATE_ACCOUNT, DELETE_ACCOUNT, UPDATE_ACCOUNT, VERIFY_LOGIN
from api_test_data import NAME, EMAIL, PASSWORD, TITLE, BIRTH_DAY, BIRTH_MONTH, BIRTH_YEAR, FIRSTNAME, LASTNAME, COMPANY, ADDRESS1, ADDRESS2, COUNTRY, STATE, CITY, ZIPCODE, MOBILE_NUMBER, UPDATED_ADDRESS1, UPDATED_ADDRESS2, UPDATED_CITY, UPDATED_ZIPCODE

@pytest.fixture(scope="session")
def base_url():
    return "https://automationexercise.com/api"

@pytest.fixture(scope="session")
def session(base_url):
    s = requests.Session()
    yield s
    s.close()

@pytest.fixture
def products_response(session, base_url):
    return session.get(f"{base_url}{PRODUCTS_LIST}")

@pytest.fixture
def brands_response(session, base_url):
    return session.get(f"{base_url}{BRANDS_LIST}")

# Creates a test account (setup) and deletes it after all tests run (teardown).
@pytest.fixture(scope="module")
def created_account(session, base_url):
    account_data = {
        "name": NAME,
        "email": EMAIL,
        "password": PASSWORD,
        "title": TITLE,
        "birth_date": BIRTH_DAY,
        "birth_month": BIRTH_MONTH,
        "birth_year": BIRTH_YEAR,
        "firstname": FIRSTNAME,
        "lastname": LASTNAME,
        "company": COMPANY,
        "address1": ADDRESS1,
        "address2": ADDRESS2,
        "country": COUNTRY,
        "state": STATE,
        "city": CITY,
        "zipcode": ZIPCODE,
        "mobile_number": MOBILE_NUMBER
    }
    
    response = session.post(f"{base_url}{CREATE_ACCOUNT}", data=account_data)
    assert response.json()["responseCode"] == 201
    
    yield {"account_data": account_data, "response": response}

    try:
        delete_response = session.delete(f"{base_url}{DELETE_ACCOUNT}", data={"email": account_data["email"], "password": account_data["password"]})
        print("\nTeardown delete response:", delete_response.status_code, delete_response.text)
    except Exception:
        pass


@pytest.fixture(scope="module")
def updated_account(created_account, session, base_url):
    account_data = created_account["account_data"]
    update_data = {
        "name": account_data["name"],
        "email": account_data["email"],
        "password": account_data["password"],
        "title": account_data["title"],
        "birth_date": account_data["birth_date"],
        "birth_month": account_data["birth_month"],
        "birth_year": account_data["birth_year"],
        "firstname": account_data["firstname"],
        "lastname": account_data["lastname"],
        "company": account_data["company"],
        "address1": UPDATED_ADDRESS1,
        "address2": UPDATED_ADDRESS2,
        "country": account_data["country"],
        "state": account_data["state"],
        "city": UPDATED_CITY,
        "zipcode": UPDATED_ZIPCODE,
        "mobile_number": account_data["mobile_number"]
    }

    response = session.put(f"{base_url}{UPDATE_ACCOUNT}", data=update_data)
    assert response.json()["responseCode"] == 200

    return {"update_data": update_data, "response": response}

@pytest.fixture(scope="module")
def deleted_account(updated_account, session, base_url):
    update_data = updated_account["update_data"]

    response = session.delete(f"{base_url}{DELETE_ACCOUNT}", data={
        "email": update_data["email"],
        "password": update_data["password"]
    })
    assert response.json()["responseCode"] == 200

    return {"deleted_email": update_data["email"], "response": response}

@pytest.fixture(scope="module")
def login_response(created_account, session, base_url):
    email = created_account["account_data"]["email"]
    password = created_account["account_data"]["password"]

    return session.post(f"{base_url}{VERIFY_LOGIN}", data={"email": email, "password": password})
