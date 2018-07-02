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
        database_name = self.app.config['DATABASE_NAME']
        database_host = self.app.config['DATABASE_HOST']
        database_username = self.app.config['DATABASE_USERNAME']
        database_password = self.app.config['DATABASE_PASSWORD']
        db_args = database_name + ' ' + database_host
        user_args = database_username + ' ' + database_password
        args = db_args + ' ' + user_args
        migrate_command = 'python ' + BASE_DIR + '/manage.py migrate ' + args
        os.system(migrate_command + ' >/dev/null 2>&1')

        self.context.push()
