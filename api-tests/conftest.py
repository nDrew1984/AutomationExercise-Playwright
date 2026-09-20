import pytest
import requests
from api_endpoints import PRODUCTS_LIST, BRANDS_LIST

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
