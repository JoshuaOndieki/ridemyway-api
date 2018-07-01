"""
    This module tests fetch user
"""
import unittest

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, USER
from ridemyway.tests.tests_v2.data import VALID_DRIVER


class TestFetchUser(V2BaseTest):
    """
        Tests fetch user API endpoint
        - Users:     '/api/v2/auth/users/<username>'         # GET
    """

    def test_fetch_user_successfully(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().get(USER)
        self.assertEqual(self.response.status_code, 200,
                         msg='Should return 200 status code for get user')

    def test_cannot_fetch_nonexistent_user(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().get(USER)
        self.assertEqual(self.response.status_code, 404,
                         msg='Should return 404 status code for get nonuser')


if __name__ == '__main__':
    unittest.main()
