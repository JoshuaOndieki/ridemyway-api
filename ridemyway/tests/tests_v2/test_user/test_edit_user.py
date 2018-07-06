"""
    This module tests edit user
"""
import unittest
import json

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN, USER
from ridemyway.tests.tests_v2.data import VALID_DRIVER


class TestEditUser(V2BaseTest):
    """
        Tests edit user API endpoint
        - Users:     '/api/v2/users'         # PUT
    """

    def test_user_can_edit_successfully(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        # Edit user
        EDITS = {
            'name': 'New Name',
        }
        self.response = self.client().put(USER,
                                          data=EDITS,
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.assertEqual(self.response.status_code, 201,
                         msg='Should return 201 status code for edits made')

    def test_cannot_edit_username(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        # Edit user
        EDITS = {
            'username': 'newer',
        }
        self.response = self.client().put(USER,
                                          data=EDITS,
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        result = json.loads(self.response.data.decode())
        self.assertIn('username', result['warnings'],
                      msg='Should not allow edits of username')

    def test_cannot_edit_usertype(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        # Edit user
        EDITS = {
            'usertype': 'rider',
        }
        self.response = self.client().put(USER,
                                           data=EDITS,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertIn('usertype', result['warnings'],
                      msg='Should not allow edits of usertype')

    def test_cannot_edit_date_joined(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        # Edit user
        EDITS = {
            'date_joined': '31/12/1901 12:00AM',
        }
        self.response = self.client().put(USER,
                                           data=EDITS,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertIn('date_joined', result['warnings'],
                      msg='Should not allow edits of date joined')


if __name__ == '__main__':
    unittest.main()
