"""
    Module for testing fetch rides
"""

import unittest
import json

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN, RIDE, VEHICLE
from ridemyway.tests.tests_v2.data import (VALID_DRIVER,
                                           VALID_RIDE,
                                           VALID_VEHICLE,
                                           VALID_DRIVER_1)


class TestCreateRide(V2BaseTest):
    """
        Tests Fetch Rides API endpoint
        - Ride:     '/api/v2/rides'                     # GET
        - Ride:     '/api/v2/rides/<ride_id>'           # GET
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

    def test_fetch_all_rides_successfully(self):
        self.create_ride()
        self.response = self.client().get(RIDE)
        self.assertEqual(self.response.status_code, 200,
                         msg='Should fetch all rides successfully')
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['message'] == 'Rides fetched successfully')

    def test_fetch_one_ride_successful(self):
        self.create_ride()
        self.response = self.client().get(RIDE + '/1')
        self.assertEqual(self.response.status_code, 200)
        result = json.loads(self.response.data.decode())
        self.assertTrue(result['message'] == 'Ride fetched successfully',
                        msg='Should fetch one ride successfully')

    def test_does_not_fetch_non_existent_ride(self):
        self.create_ride()
        self.response = self.client().get(RIDE + '/6454')
        self.assertEqual(self.response.status_code, 404,
                         msg='404 for non existent rides')

    def test_cannot_fetch_taken_rides(self):
        access_token = self.create_ride()
        # Mark ride as taken
        self.response = self.client().put(RIDE + '/1',
                                          data={'status': 'taken'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.response = self.client().get(RIDE)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['meta']['rides'], 0,
                         msg='Should not fetch taken ride')

    def test_cannot_fetch_canncelled_rides(self):
        access_token = self.create_ride()
        # Mark ride as cancelled
        self.response = self.client().put(RIDE + '/1',
                                          data={'status': 'cancelled'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.response = self.client().get(RIDE)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['meta']['rides'], 0,
                         msg='Should not fetch cancelled ride')

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
