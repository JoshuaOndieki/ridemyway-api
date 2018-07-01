"""
    Module for testing create ride
"""

import unittest
import json

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN, RIDE, VEHICLE
from ridemyway.tests.tests_v2.data import (VALID_RIDER,
                                           VALID_DRIVER,
                                           VALID_RIDE,
                                           INVALID_RIDE_DATE,
                                           PAST_RIDE_DATE,
                                           VALID_VEHICLE,
                                           INVALID_RIDE_COST,
                                           INVALID_RIDE_CAPACITY,
                                           VALID_DRIVER_1,
                                           GREATER_RIDE_CAPACITY)


class TestCreateRide(V2BaseTest):
    """
        Tests Create Ride API endpoint
        - Ride:     '/api/v2/rides'         # POST
    """

    def authenticate(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        return access_token

    def create_vehicle(self, access_token):
        self.client().post(VEHICLE, data=VALID_VEHICLE,
                           headers=dict(
                               Authorization="Bearer " + access_token))

    def test_creates_a_ride_successfully_with_valid_data(self):
        access_token = self.authenticate()
        self.create_vehicle(access_token)
        self.response = self.client().post(RIDE, data=VALID_RIDE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'],
                         'Ride created successfully',
                         msg='Given the correct details, the ride should be created successfully!')
        self.assertEqual(self.response.status_code, 201)

    def test_does_not_create_ride_with_invalid_date(self):
        access_token = self.authenticate()
        self.create_vehicle(access_token)
        self.response = self.client().post(RIDE, data=INVALID_RIDE_DATE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['date'],
                         'Date of departure is in invalid format',
                         msg='Should only accept correctly formatted dates!')
        self.assertEqual(self.response.status_code, 400)

    def test_cannot_create_ride_with_passed_date(self):
        access_token = self.authenticate()
        self.create_vehicle(access_token)
        self.response = self.client().post(RIDE, data=PAST_RIDE_DATE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['date'],
                         'Date of departure is in the past',
                         msg='Should only accept future dates!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_invalid_cost(self):
        access_token = self.authenticate()
        self.create_vehicle(access_token)
        self.response = self.client().post(RIDE, data=INVALID_RIDE_COST,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['cost'],
                         'Invalid cost given',
                         msg='The cost should be a number!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_invalid_capacity(self):
        access_token = self.authenticate()
        self.create_vehicle(access_token)
        self.response = self.client().post(RIDE, data=INVALID_RIDE_CAPACITY,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['capacity'],
                         'Invalid capacity given',
                         msg='The capacity should be an integer!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_above_max_capacity(self):
        access_token = self.authenticate()
        self.create_vehicle(access_token)
        self.response = self.client().post(RIDE, data=GREATER_RIDE_CAPACITY,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['capacity'],
                         'Capacity greater than specified on vehicle',
                         msg='The capacity should be equal or less than vehicle!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_non_registered_vehicle(self):
        access_token = self.authenticate()
        self.response = self.client().post(RIDE, data=VALID_RIDE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['vehicle'],
                         'Vehicle not registered',
                         msg='Vehicle should be registered first!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_vehicle_not_owned(self):
        access_token = self.authenticate()
        self.create_vehicle(access_token)
        self.client().post(SIGNUP, data=VALID_DRIVER_1)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER_1)
        access_token = self.response.access_token
        self.response = self.client().post(RIDE, data=VALID_RIDE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['vehicle'],
                         'You do not own this vehicle',
                         msg='Vehicle should be owned!')
        self.assertEqual(self.response.status_code, 400)

    def test_only_drivers_can_create_rides(self):
        self.client().post(SIGNUP, data=VALID_RIDER)
        access_token = self.response = self.client().post(LOGIN, data=VALID_RIDER)
        self.response = self.client().post(RIDE, data=VALID_RIDE,
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'],
                         'Only drivers can create rides',
                         msg='Should not allow riders to create rides!')
        self.assertEqual(self.response.status_code, 403)

    def test_anonymous_users_cannot_create_rides(self):
        self.response = self.client().post(RIDE, data=VALID_RIDE)
        self.assertEqual(self.response.status_code, 401,
                         msg='Anonymous users cannot create rides!')


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
