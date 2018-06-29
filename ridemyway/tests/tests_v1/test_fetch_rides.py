"""
    Module for testing fetch rides
"""

import json
import unittest

from ridemyway.tests import BaseTest
from . import VALID_RIDE_DATASET, VALID_RIDE_DATASET_1


class TestFetchRideAPIEndpoint(BaseTest):
    """
        Tests Fetch Ride API endpoint
        - Ride:     '/api/v1/rides'             # GET
        - Ride:     '/api/v1/rides/<rideId>'    # GET
    """

    def setUp(self):
        """
            Set up tests
        """
        super().setUp()
        # Create rides for testing
        self.client().post('/api/v1/rides', data=VALID_RIDE_DATASET)
        self.client().post('/api/v1/rides', data=VALID_RIDE_DATASET_1)

    def test_fetches_rides_successfully(self):
        """
            Test rides are fetched successfully
        """
        self.response = self.client().get('/api/v1/rides')
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'],
                         'Rides fetched successfully',
                         msg='Should fetch rides successfully!')
        self.assertEqual(self.response.status_code, 200)

    def test_fetches_a_single_ride_with_valid_id(self):
        """
            Test a single ride can be fetched successfully
        """
        self.response = self.client().get('/api/v1/rides/1')
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'],
                         'Ride fetched successfully',
                         msg='Should fetch single ride given a valid ride id!')
        self.assertEqual(self.response.status_code, 200)

    def test_does_not_fetch_ride_that_does_not_exist(self):
        """
            Test fetching non existent ride edge case
        """
        self.response = self.client().get('/api/v1/rides/6454')
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['status'], 'failed',
                         msg='Should only fetch existing rides!')
        self.assertEqual(self.response.status_code, 404)

    def test_does_not_fetch_wrong_ride(self):
        """
            Test the correct ride is fetched
        """
        self.response = self.client().get('/api/v1/rides/1')
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['data']['ride_id'], 1,
                         msg='Should be able to fetch the correct ride\
                          with the id given in the url!')


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
