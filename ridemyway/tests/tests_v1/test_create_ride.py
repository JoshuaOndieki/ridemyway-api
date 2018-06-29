"""
    Module for testing create ride
"""

import unittest
import json

from ridemyway.tests import BaseTest
from . import (VALID_RIDE_DATASET,
               INVALID_DATE_DATASET,
               PAST_DATE_DATASET,
               INVALID_COST_DATASET,
               INVALID_CAPACITY_DATASET,
               INVALID_VEHICLE_NUMBER_PLATE)


class TestCreateRideAPIEndpoint(BaseTest):
    """
        Tests Create Ride API endpoint
        - Ride:     '/api/v1/rides'         # POST
    """

    def test_creates_a_ride_successfully_with_valid_data(self):
        """
            Test success creating a ride
        """
        self.response = self.client().post('/api/v1/rides', data=VALID_RIDE_DATASET)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'],
                         'Ride created successfully',
                         msg='Given the correct details,\
                         the ride should be created successfully!')
        self.assertEqual(self.response.status_code, 201)

    def test_does_not_create_ride_with_invalid_date(self):
        """
            Test invalid date edge case on creating a ride
        """
        self.response = self.client().post('/api/v1/rides', data=INVALID_DATE_DATASET)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['date'],
                         'Date of departure is in invalid format',
                         msg='Should only accept correctly formatted dates!')
        self.assertEqual(self.response.status_code, 400)

    def test_cannot_create_ride_with_passed_date(self):
        """
            Test past dates are not allowed on new rides
        """
        self.response = self.client().post('/api/v1/rides', data=PAST_DATE_DATASET)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['date'],
                         'Date of departure is in the past',
                         msg='Should only accept future dates!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_invalid_cost(self):
        """
            Test invalid cost edge case
        """
        self.response = self.client().post('/api/v1/rides', data=INVALID_COST_DATASET)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['cost'],
                         'Invalid cost given',
                         msg='The cost should be a number!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_invalid_capacity(self):
        """
            Test invalid capacity edge case
        """
        self.response = self.client().post('/api/v1/rides', data=INVALID_CAPACITY_DATASET)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['capacity'],
                         'Invalid capacity given',
                         msg='Capacity should be a number!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_invalid_vehicle_number_plate(self):
        """
            Test invalid vehicle number plate edge case
        """
        self.response = self.client().post('/api/v1/rides', data=INVALID_VEHICLE_NUMBER_PLATE)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['vehicleNumberPlate'],
                         'Invalid vehicle number plate given',
                         msg='vehicle Number Plate should be a string!')
        self.assertEqual(self.response.status_code, 400)


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
