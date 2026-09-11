import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://automationexercise.com/api"

@pytest.fixture(scope="session")
def session(base_url):
    s = requests.Session()
    yield s
    s.close()
