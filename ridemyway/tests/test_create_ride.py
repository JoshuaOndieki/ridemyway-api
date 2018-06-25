import unittest
import json
from ridemyway import create_app


class TestCreateRideAPIEndpoints(unittest.TestCase):
    """
        Tests Create Ride API endpoint
        - Ride:     '/api/v1/rides'         # POST
    """

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.headers = {'content-type': 'application/json'}
        self.context = self.app.app_context()
        self.context.push()

    def tearDown(self):
        self.context.pop()


# Just incase a testing library is not used!
if __name__ is "__main__":
    unittest.main()
