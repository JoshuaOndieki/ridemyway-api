"""
    Module for testing add vehicle
"""

import unittest
import json

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN, VEHICLE
from ridemyway.tests.tests_v2.data import (VALID_RIDER,
                                           VALID_DRIVER,
                                           VALID_VEHICLE,
                                           INVALID_VEHICLE_CAPACITY)


class TestCreateVehicle(V2BaseTest):
    """
        Tests Add Vehicle API endpoint
        - Ride:     '/api/v2/vehicle'         # POST
    """

    def authenticate(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        return access_token

    def test_add_vehicle_successful(self):
        access_token = self.authenticate()
        self.response = self.client().post(VEHICLE, data=VALID_VEHICLE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 201,
                         msg='Should create a vehicle successfully!')

    def test_doesnot_allow_duplicate_vehicles(self):
        access_token = self.authenticate()
        self.client().post(VEHICLE, data=VALID_VEHICLE,
                           headers=dict(
                               Authorization="Bearer " + access_token))
        self.response = self.client().post(VEHICLE, data=VALID_VEHICLE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 409,
                         msg='Should not add duplicate vehicles!')

    def test_add_vehicle_unsuccessful_with_rider(self):
        self.client().post(SIGNUP, data=VALID_RIDER)
        self.response = self.client().post(LOGIN, data=VALID_RIDER)
        access_token = self.response.access_token
        self.response = self.client().post(VEHICLE, data=VALID_VEHICLE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'],
                         'Only drivers can add vehicles',
                         msg='Only drivers can add vehicles!')
        self.assertEqual(self.response.status_code, 403)

    def test_does_not_add_vehicle_with_invalid_capacity(self):
        access_token = self.authenticate()

        self.response = self.client().post(VEHICLE, data=INVALID_VEHICLE_CAPACITY,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['capacity'],
                         'Capacity is in invalid format',
                         msg='Should only accept integer capacity!')
        self.assertEqual(self.response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
