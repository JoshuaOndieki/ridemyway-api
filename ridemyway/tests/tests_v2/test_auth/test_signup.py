"""
    This module tests signup
"""
import unittest
import json

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP
from ridemyway.tests.tests_v2.data import (VALID_RIDER,
                                           VALID_DRIVER,
                                           SPECIAL_CHARS_USERNAME,
                                           SPECIAL_CHARS_NAME,
                                           INVALID_EMAIL,
                                           INVALID_CONTACTS,
                                           INVALID_USERTYPE,
                                           INVALID_GENDER)


class TestSignUp(V2BaseTest):
    """
        Tests signup API endpoint
        - Ride:     '/api/v2/auth/signup'         # POST
    """

    def test_driver_can_signup_successfully(self):
        self.response = self.client().post(SIGNUP, data=VALID_DRIVER)
        self.assertEqual(self.response.status_code, 201,
                        msg='Should return 201 status code for successful driver creation')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'success',
                        msg='Should return status success in response data')

    def test_rider_can_signup_successfully(self):
        self.response = self.client().post(SIGNUP, data=VALID_RIDER)
        self.assertEqual(self.response.status_code, 201,
                        msg='Should return 201 status code for successful rider creation')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'success',
                        msg='Should return status success in response data')

    def test_does_not_allow_duplicate_users(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(SIGNUP, data=VALID_DRIVER)
        self.assertEqual(self.response.status_code, 409,
                        msg='Should return 409 status code for duplicate attempt')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_no_special_chars_allowed_in_username(self):
        self.response = self.client().post(SIGNUP,
                                           data=SPECIAL_CHARS_USERNAME)
        self.assertEqual(self.response.status_code, 422,
                        msg='Should return 422 status code for special chars in username')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_no_special_chars_allowed_in_name(self):
        self.response = self.client().post(SIGNUP,
                                           data=SPECIAL_CHARS_NAME)
        self.assertEqual(self.response.status_code, 422,
                        msg='Should return 422 status code for special chars in name')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_does_not_allow_invalid_email_formats(self):
        self.response = self.client().post(SIGNUP, data=INVALID_EMAIL)
        self.assertEqual(self.response.status_code, 422,
                        msg='Should return 422 status code for invalid email')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_required_data(self):
        self.response = self.client().post(SIGNUP, data={})
        self.assertEqual(self.response.status_code, 400,
                        msg='Should return 400 status code for empty data')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_contacts_is_a_number(self):
        self.response = self.client().post(SIGNUP, data=INVALID_CONTACTS)
        self.assertEqual(self.response.status_code, 422,
                        msg='Should return 422 status code for invalid contacts')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_unknown_usertypes_not_allowed(self):
        self.response = self.client().post(SIGNUP, data=INVALID_USERTYPE)
        self.assertEqual(self.response.status_code, 422,
                        msg='Should return 422 status code for invalid usertype')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')

    def test_unknown_gender_types_not_allowed(self):
        self.response = self.client().post(SIGNUP, data=INVALID_GENDER)
        self.assertEqual(self.response.status_code, 422,
                        msg='Should return 422 status code for invalid gender')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['status'] == 'failed',
                        msg='Should return status failed in response data')


if __name__ == '__main__':
    unittest.main()
