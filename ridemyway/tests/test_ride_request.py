import unittest
import json
from ridemyway import create_app


class TestCreateRideRequestAPIEndpoint(unittest.TestCase):
    """
        Tests Create Ride Request API endpoint
        - Ride:     '/api/v1/rides/<rideId>/requests'   # POST
    """

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.headers = {'content-type': 'application/json'}
        self.context = self.app.app_context()
        self.context.push()
        data = {
            'data': [
                {'departure': 'Jun 25 2018  1:30PM',
                 'origin': 'Nairobi',
                 'destination': 'Garissa',
                 'cost': 350,
                 'vehicle_number_plate': 'KBC-A21',
                 'capacity': 3
                 },
                {'departure': 'Jun 28 2018  7:00AM',
                 'origin': 'Garissa',
                 'destination': 'Nairobi',
                 'cost': 500,
                 'vehicle_number_plate': 'KBC-A21',
                 'capacity': 3
                 }
                ]
            }

        self.client().post('/api/v1/rides', data=data)

    def tearDown(self):
        self.context.pop()

    def test_creates_a_ride_request_successfully_with_existing_ride(self):
        self.response = self.client().post('/api/v1/rides/1/requests')
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['message'], 'Ride request created successfully')
        self.assertEqual(self.response.status_code, 201)

    def test_does_not_create_a_request_to_nonexistent_ride(self):
        self.response = self.client().get('/api/v1/rides/6454')
        result = json.loads(self.response.data.decode())
        self.assertEqual(result['status'], 'failed')
        self.assertEqual(self.response.status_code, 404)


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
