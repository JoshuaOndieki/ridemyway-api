"""
    This module tests logout
"""
import unittest
import json

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN, LOGOUT
from ridemyway.tests.tests_v2.data import VALID_DRIVER


class TestLogout(V2BaseTest):
    """
        Tests logout API endpoint
        - Auth:     '/api/v2/auth/logout'         # POST
    """

    def test_user_can_logout_successfully(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        result = json.loads(self.response.data.decode())
        access_token = result['access_token']
        self.response = self.client().post(LOGOUT,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        # Attempt to logout again
        self.response = self.client().post(LOGOUT,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 400,
                         msg='Should return 400 status code for' +
                         ' use of blacklisted token')


if __name__ == '__main__':
    unittest.main()
