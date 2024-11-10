import pytest
import requests

# Base URL for the HTTPBin API
BASE_URL = "https://httpbin.org"

@pytest.fixture(scope="module")
def setup_module():
    """Module-level setup (replaces setUpClass)"""
    print("Setting up module resources...")
    # Example: Initialize a session or shared resources
    session = requests.Session()
    yield session
    print("Tearing down module resources...")
    session.close()

@pytest.fixture(scope="function")
def setup_function():
    """Function-level setup (replaces setUp)"""
    print("Setting up for test...")

@pytest.fixture(scope="function", autouse=True)
def teardown_function():
    """Function-level teardown (replaces tearDown)"""
    yield
    print("Tearing down after test...")

def test_get_request(setup_module, setup_function):
    url = f"{BASE_URL}/get"
    response = setup_module.get(url)
    assert response.status_code == 200
    print("GET request status code:", response.status_code)

def test_post_request(setup_module, setup_function):
    url = f"{BASE_URL}/post"
    payload = {"name": "ChatGPT", "role": "AI"}
    response = setup_module.post(url, json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert "json" in response_json
    assert response_json["json"] == payload
    print("POST request status code:", response.status_code)
    print("POST request response json:", response_json["json"])

def test_delayed_response(setup_module, setup_function):
    delay_time = 3  # seconds
    url = f"{BASE_URL}/delay/{delay_time}"
    response = setup_module.get(url)
    assert response.status_code == 200
    print("Delayed request status code:", response.status_code)

def test_negative_scenario(setup_module, setup_function):
    url = f"{BASE_URL}/status/404"
    response = setup_module.get(url)
    assert response.status_code == 404
    print("Negative scenario status code:", response.status_code)

def test_unauthorized_access(setup_module, setup_function):
    url = f"{BASE_URL}/basic-auth/user/passwd"
    response = setup_module.get(url, auth=('user', 'wrongpassword'))
    assert response.status_code == 401
    print("Unauthorized access status code:", response.status_code)
