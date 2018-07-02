"""
    Module for testing ride status update
"""

import unittest

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN, RIDE, VEHICLE
from ridemyway.tests.tests_v2.data import (VALID_DRIVER,
                                           VALID_RIDE,
                                           VALID_VEHICLE,
                                           VALID_DRIVER_1)


class TestRideStatus(V2BaseTest):
    """
        Tests Ride Status Update API endpoint
        - Ride:     '/api/v2/rides/<ride_id>'         # PUT
    """

    def create_ride(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        self.client().post(VEHICLE, data=VALID_VEHICLE,
                           headers=dict(
                               Authorization="Bearer " + access_token))
        self.response = self.client().post(RIDE, data=VALID_RIDE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        return access_token

    def test_take_ride_successfully(self):
        access_token = self.create_ride()
        self.response = self.client().put(RIDE + '/1',
                                          data={'status': 'taken'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.assertEqual(self.response.status_code, 200,
                         msg='The ride should be taken successfully')

    def test_cancel_ride_successfully(self):
        access_token = self.create_ride()
        self.response = self.client().put(RIDE + '/1',
                                          data={'status': 'cancelled'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.assertEqual(self.response.status_code, 200,
                         msg='The ride should be cancelled successfully')

    def test_setting_unknown_status_unsuccessful(self):
        access_token = self.create_ride()
        self.response = self.client().put(RIDE + '/1',
                                          data={'status': 'unknown status'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.assertEqual(self.response.status_code, 200,
                         msg='Should only allow taken/cancelled status update')

    def test_only_creater_can_update_ride_status(self):
        self.create_ride()
        self.client().post(SIGNUP, data=VALID_DRIVER_1)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER_1)
        access_token = self.response.access_token
        self.response = self.client().put(RIDE + '/1',
                                          data={'status': 'cancelled'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.assertEqual(self.response.status_code, 403,
                         msg='Only creators can update ride status')


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
