"""
    Module for testing ride requests
"""

import unittest
import json

from ridemyway.tests.tests_v1 import V1BaseTest
from . import VALID_RIDE_DATASET, VALID_RIDE_DATASET_1


class TestCreateRideRequestAPIEndpoint(V1BaseTest):
    """
        Tests Create Ride Request API endpoint
        - Ride:     '/api/v1/rides/<rideId>/requests'   # POST
    """
    def setUp(self):
        """
            Set up tests
        """
        super().setUp()
        self.client().post('/api/v1/rides', data=VALID_RIDE_DATASET)
        self.client().post('/api/v1/rides', data=VALID_RIDE_DATASET_1)

    def test_creates_a_ride_request_successfully_with_existing_ride(self):
        """
            Test ride request is created successfully for existing rides
        """
        self.response = self.client().post('/api/v1/rides/1/requests')
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'],
                         'Ride request created successfully',
                         msg='Should successfully create a ride request\
                          given an existing ride!')
        self.assertEqual(self.response.status_code, 201)

    def test_does_not_create_a_request_to_nonexistent_ride(self):
        """
            Test requests to non existing rides edge case
        """
        self.response = self.client().get('/api/v1/rides/6454')
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['status'], 'failed',
                         msg='Should only accept requests for existing rides!')
        self.assertEqual(self.response.status_code, 404)


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
