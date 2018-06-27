"""
    Module for testing create ride
"""

import unittest
import json
from ridemyway import create_app


class TestCreateRideAPIEndpoint(unittest.TestCase):
    """
        Tests Create Ride API endpoint
        - Ride:     '/api/v1/rides'         # POST
    """

    def setUp(self):
        """
            Set up tests
        """
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.headers = {'content-type': 'application/json'}
        self.context = self.app.app_context()
        self.context.push()

    def tearDown(self):
        """
            Teardown all test files and instances created
        """
        self.context.pop()

    def test_creates_a_ride_successfully_with_valid_data(self):
        """
            Test sucess creating a ride
        """
        data = {
            'departure': 'Jun 25 6454  1:30PM',
            'origin': 'Nairobi',
            'destination': 'Garissa',
            'cost': 350, 'vehicle_number_plate':
            'KBC-A21', 'capacity': 3
            }

        self.response = self.client().post('/api/v1/rides', data=data)
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
        data = {
            'departure': 'Not a date',
            'origin': 'Nairobi',
            'destination': 'Garissa',
            'cost': 350, 'vehicle_number_plate':
            'KBC-A21', 'capacity': 3
            }

        self.response = self.client().post('/api/v1/rides', data=data)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['date'],
                         'Date of departure is in invalid format',
                         msg='Should only accept correctly formatted dates!')
        self.assertEqual(self.response.status_code, 400)

    def test_cannot_create_ride_with_passed_date(self):
        """
            Test passed dates are not allowed on new rides
        """
        data = {
            'departure': 'Jun 25 1901  1:30PM',
            'origin': 'Nairobi',
            'destination': 'Garissa',
            'cost': 350, 'vehicle_number_plate':
            'KBC-A21', 'capacity': 3
            }

        self.response = self.client().post('/api/v1/rides', data=data)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['date'],
                         'Date of departure is in the past',
                         msg='Should only accept future dates!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_invalid_cost(self):
        """
            Test invalid cost edge case
        """
        data = {
            'departure': 'Jun 25 2018  1:30PM',
            'origin': 'Nairobi',
            'destination': 'Garissa',
            'cost': '%^$', 'vehicle_number_plate':
            'KBC-A21', 'capacity': 3
            }

        self.response = self.client().post('/api/v1/rides', data=data)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['cost'],
                         'Invalid cost given',
                         msg='The cost should be a number!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_invalid_capacity(self):
        """
            Test invalid capacity edge case
        """
        data = {
            'departure': 'Jun 25 2018  1:30PM',
            'origin': 'Nairobi',
            'destination': 'Garissa',
            'cost': 350, 'vehicle_number_plate':
            'KBC-A21', 'capacity': 'hundred'
            }

        self.response = self.client().post('/api/v1/rides', data=data)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['capacity'],
                         'Invalid capacity given',
                         msg='Capacity should be a number!')
        self.assertEqual(self.response.status_code, 400)

    def test_does_not_create_ride_with_invalid_vehicle_number_plate(self):
        """
            Test invalid vehicle number plate edge case
        """
        data = {
            'departure': 'Jun 25 2018  1:30PM',
            'origin': 'Nairobi',
            'destination': 'Garissa',
            'cost': 350, 'vehicle_number_plate':
            2121, 'capacity': 3
            }
        self.response = self.client().post('/api/v1/rides', data=data)
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['errors']['vehicleNumberPlate'],
                         'Invalid vehicle number plate given',
                         msg='vehicle Number Plate should be a string!')
        self.assertEqual(self.response.status_code, 400)


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
