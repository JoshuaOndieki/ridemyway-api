"""
    This module tests login
"""
import unittest
import json

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN
from ridemyway.tests.tests_v2.data import VALID_DRIVER


class TestLogin(V2BaseTest):
    """
        Tests login API endpoint
        - Auth:     '/api/v2/auth/login'         # POST
    """
    def signup(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)

    def test_user_can_login_successfully(self):
        self.signup()
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        self.assertEqual(self.response.status_code, 200,
                         msg='Should return 200 status code for successful login')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['access_token'] is not False,
                        msg='Should return access token')

    def test_non_user_cannot_login(self):
        NON_USER = {
            'username': 'null',
            'password': 'null[pass]'
        }
        self.response = self.client().post(LOGIN, data=NON_USER)
        self.assertEqual(self.response.status_code, 401,
                         msg='Should return 401 status code for non users')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_non_matching_credentials_not_authorized(self):
        self.signup()
        FAKE_PASSWORD = {
            'username': 'driver',
            'password': 'fake[pass]'
        }
        self.response = self.client().post(LOGIN, data=FAKE_PASSWORD)
        self.assertEqual(self.response.status_code, 401,
                         msg='Should return 401 status code for fake users')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_required_details_are_provided(self):
        self.response = self.client().post(LOGIN, data={})
        self.assertEqual(self.response.status_code, 400,
                         msg='Should return 400 status code for empty data')


if __name__ == '__main__':
    unittest.main()
