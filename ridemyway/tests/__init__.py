"""
    BASE testing module
"""

import unittest
from ridemyway import create_app


class BaseTest(unittest.TestCase):
    """
        Base class for testing
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
