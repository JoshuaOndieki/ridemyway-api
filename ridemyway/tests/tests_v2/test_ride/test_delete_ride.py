"""
    Module for testing delete ride
"""

import unittest

from ridemyway.tests.tests_v2 import V2BaseTest
from ridemyway.tests.tests_v2.urls import SIGNUP, LOGIN, RIDE, VEHICLE
from ridemyway.tests.tests_v2.data import (VALID_DRIVER,
                                           VALID_RIDE,
                                           VALID_VEHICLE,
                                           VALID_DRIVER_1)


class TestDeleteRide(V2BaseTest):
    """
        Tests Delete Ride API endpoint
        - Ride:     '/api/v2/rides/<ride_id>'         # DEL
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

    def test_delete_ride_successfully(self):
        access_token = self.create_ride()
        self.response = self.client().delete(RIDE + '/1',
                                             headers=dict(
                                                 Authorization="Bearer " +
                                                 access_token))
        self.assertEqual(self.response.status_code, 204,
                        msg='The ride should be deleted successfully')

    def test_delete_ride_by_non_creater_unsuccessful(self):
        self.create_ride()
        self.client().post(SIGNUP, data=VALID_DRIVER_1)
        self.response = self.client().post(LOGIN, data=VALID_DRIVER_1)
        access_token = self.response.access_token
        self.response = self.client().delete(RIDE + '/1',
                                             headers=dict(
                                                 Authorization="Bearer " +
                                                 access_token))
        self.assertEqual(self.response.status_code, 403,
                         msg='The ride should only be deleted by creater')

    def test_delete_ride_deletes_all_requests(self):
        access_token = self.create_ride()
        # Create a request
        self.client().post(RIDE + '/1/requests',
                           headers=dict(
                               Authorization="Bearer " +
                               access_token))
        self.client().delete(RIDE + '/1',
                             headers=dict(
                                 Authorization="Bearer " +
                                 access_token))
        # Try to accept request
        self.response = self.client().put(RIDE + '/1/requests/1',
                                          data={'action': 'accept'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))

        self.assertEqual(self.response.status_code, 404,
                         msg='Request should be cascade deleted with ride!')

    def test_cannot_delete_taken_rides(self):
        access_token = self.create_ride()
        # Mark ride as taken
        self.response = self.client().put(RIDE, data={'status': 'taken'},
                                          headers=dict(
                                              Authorization="Bearer " +
                                              access_token))
        # Try to delete it
        self.response = self.client().delete(RIDE + '/1',
                                             headers=dict(
                                                 Authorization="Bearer " +
                                                 access_token))
        self.assertEqual(self.response.status_code, 405,
                         msg='Once a ride is taken, it cannot be deleted!')


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
