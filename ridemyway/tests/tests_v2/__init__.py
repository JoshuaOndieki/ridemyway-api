"""
    Version 2 BASE testing module
"""
import os

from ridemyway.tests import BaseTest


class V2BaseTest(BaseTest):
    """
        v2 Base class for testing
    """
    def setUp(self):
        """
            Set up tests
        """
        super().setUp()

        # Do migrations
        BASE_DIR = self.app.config['BASE_DIR']
        makemigrations_cmd = 'python ' + BASE_DIR + '/manage.py makemigrations'
        migrate_cmd = 'python ' + BASE_DIR + '/manage.py migrate'
        os.system(makemigrations_cmd + ' >/dev/null 2>&1')
        os.system(migrate_cmd + ' >/dev/null 2>&1')

        self.context.push()
