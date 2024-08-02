import unittest
import requests

class TestHttpBinAPI(unittest.TestCase):
    base_url = "https://httpbin.org"

    @classmethod
    # Set up any shared resources here, e.g., creating a session, preparing data
    def setUpClass(cls):

    @classmethod
    # Clean up any shared resources here, e.g., closing a session, deleting data
    def tearDownClass(cls):

    # Set up resources needed for each test, e.g., initialize variables
    def setUp(self):

    # Clean up resources after each test, e.g., reset variables
    def tearDown(self):


    def test_get_request(self):
        url = f"{self.base_url}/get"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print("GET request status code:", response.status_code)

    def test_post_request(self):
        url = f"{self.base_url}/post"
        payload = {"name": "ChatGPT", "role": "AI"}
        response = requests.post(url, json=payload)
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertIn("json", response_json)
        self.assertEqual(response_json["json"], payload)
        print("POST request status code:", response.status_code)
        print("POST request response json:", response_json["json"])

    def test_delayed_response(self):
        delay_time = 3  # seconds
        url = f"{self.base_url}/delay/{delay_time}"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print("Delayed request status code:", response.status_code)

    def test_negative_scenario(self):
        url = f"{self.base_url}/status/404"
        response = requests.get(url)
        self.assertEqual(response.status_code, 404)
        print("Negative scenario status code:", response.status_code)

    def test_unauthorized_access(self):
        url = f"{self.base_url}/basic-auth/user/passwd"
        response = requests.get(url, auth=('user', 'wrongpassword'))
        self.assertEqual(response.status_code, 401)
        print("Unauthorized access status code:", response.status_code)

if __name__ == "__main__":
    unittest.main()

