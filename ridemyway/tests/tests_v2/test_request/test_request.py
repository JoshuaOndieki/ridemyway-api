"""
    Module for testing requests
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
        - Ride:     '/api/v2/rides/<ride_id>/requests'              # POST
        - Ride:     '/api/v2/rides/<ride_id>/requests/request_id'   # PUT
        - Ride:     '/api/v2/rides/<ride_id>/requests/request_id'   # DEL
    """

    def authenticate(self):
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        return access_token

    def add_vehicle(self, access_token):
        self.client().post(VEHICLE, data=VALID_VEHICLE,
                           headers=dict(
                               Authorization="Bearer " + access_token))

    def create_ride(self):
        access_token = self.authenticate()
        self.create_vehicle(access_token)
        self.client().post(RIDE, data=VALID_RIDE,
                           headers=dict(
                                Authorization="Bearer " +
                                access_token))
        return access_token

    def test_creates_request_successfully(self):
        self.create_ride()
        self.client().post(SIGNUP, data=VALID_RIDER)
        self.response = self.client().post(LOGIN, data=VALID_RIDER)
        access_token = self.response.access_token
        self.response = self.client().post(RIDE + '/1/requests',
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 201,
                         msg='Should create request successfully')

    def test_driver_cannot_create_request(self):
        access_token = self.create_ride()
        self.response = self.client().post(RIDE + '/1/requests',
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 403,
                         msg='Only riders can make requests')

    def test_request_can_only_be_made_to_existing_rides(self):
        self.client().post(SIGNUP, data=VALID_RIDER)
        self.response = self.client().post(LOGIN, data=VALID_RIDER)
        access_token = self.response.access_token
        self.response = self.client().post(RIDE + '/1/requests',
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 404,
                         msg='Cannot request a 404 ride')

    def test_request_cannot_be_made_to_taken_rides(self):
        self.create_ride()
        self.client().post(SIGNUP, data=VALID_RIDER)
        self.response = self.client().post(LOGIN, data=VALID_RIDER)
        access_token = self.response.access_token
        # Mark ride as taken
        self.response = self.client().put(RIDE + '/1',
                                          data={'status': 'taken'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.response = self.client().post(RIDE + '/1/requests',
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 423,
                         msg='Cannot request a taken ride')

    def test_request_cannot_be_made_to_cancelled_rides(self):
        self.create_ride()
        self.client().post(SIGNUP, data=VALID_RIDER)
        self.response = self.client().post(LOGIN, data=VALID_RIDER)
        access_token = self.response.access_token
        # Mark ride as cancelled
        self.response = self.client().put(RIDE + '/1',
                                          data={'status': 'cancelled'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.response = self.client().post(RIDE + '/1/requests',
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 423,
                         msg='Cannot request a cancelled ride')

    def test_cannot_request_ride_with_capacity_greater_than_available(self):
        self.create_ride()
        self.client().post(SIGNUP, data=VALID_RIDER)
        self.response = self.client().post(LOGIN, data=VALID_RIDER)
        access_token = self.response.access_token
        self.response = self.client().post(RIDE + '/1/requests',
                                           data={'capacity': 4},
                                           headers=dict(
                                               Authorization="Bearer " +
                                               access_token))
        self.assertEqual(self.response.status_code, 400,
                         msg='Should not allow requests exiding set capacity!')

    def test_non_ride_creator_cannot_accept_requests(self):
        self.create_ride()
        self.client().post(SIGNUP, data=VALID_RIDER)
        self.response = self.client().post(LOGIN, data=VALID_RIDER)
        access_token = self.response.access_token
        self.client().post(RIDE + '/1/requests',
                           data={'capacity': 2},
                           headers=dict(
                               Authorization="Bearer " +
                               access_token))
        self.response = self.client().put(RIDE + '/1/requests/1',
                                          data={'action': 'accept'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        self.assertEqual(self.response.status_code, 403,
                         msg='Only ride creators can accept requests!')

    def test_non_requester_cannot_delete_request(self):
        self.create_ride()
        self.client().post(SIGNUP, data=VALID_RIDER)
        self.response = self.client().post(LOGIN, data=VALID_RIDER)
        access_token = self.response.access_token
        self.client().post(RIDE + '/1/requests',
                           data={'capacity': 2},
                           headers=dict(
                               Authorization="Bearer " +
                               access_token))
        self.client().post(SIGNUP, data=VALID_DRIVER)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER)
        access_token = self.response.access_token
        self.response = self.client().delete(RIDE + '/1/requests/1',
                                             headers=dict(
                                                 Authorization="Bearer " +
                                                 access_token))
        self.assertEqual(self.response.status_code, 403,
                         msg='Only requesters can delete requests!')


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
