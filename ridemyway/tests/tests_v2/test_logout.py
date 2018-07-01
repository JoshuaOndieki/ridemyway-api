"""
    This module tests login
"""
import unittest

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN, RIDE
from ridemyway.tests.tests_v2.data import VALID_DRIVER, VALID_RIDE


class TestLogout(V2BaseTest):
    """
        Tests logout API endpoint
        - Auth:     '/api/v2/auth/logout'         # POST
    """

    def test_user_can_logout_successfully(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        # Attempt to do a protected action
        self.response = self.client().post(RIDE,
                                           data=VALID_RIDE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 401,
                         msg='Should return 401 status code for unauthorized')


if __name__ == '__main__':
    unittest.main()
