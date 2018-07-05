"""
    Controller for endpoints on auth
"""

from datetime import datetime
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from ridemyway.utils.response import Response
from ridemyway.utils.db_queries import insert_user
from ridemyway.api.v2.models.user import User
from ridemyway.utils.db_queries import select_user


class AuthController():
    """
        Controls all CRUD operations of the User object about Authentication.
    """

    def signup(self, **kwargs):
        """
            Controls the signup process
        """
        now = datetime.now()
        kwargs['date_joined'] = now.strftime('%b %d %Y %H:%M%p')
        self.user = User(kwargs)
        user_exists = select_user(username=self.user.username,
                                  email=self.user.email)
        if user_exists:
            return Response.failed(message='Such user exists'), 409
        user_added = insert_user(self.user)
        message = 'User created successfully'
        attributes = {
            'location': '/api/v2/users/' + self.user.username
        }
        if user_added:
            return Response.success(message=message, attributes=attributes), 201
        return Response.failed(message='failed to add user'), 400

    def login(self, **kwargs):
        """
            Controls the login process
        """
        username = None
        email = None
        if 'username' in kwargs:
            username = kwargs['username']
        if 'email' in kwargs:
            email = kwargs['email']
        self.user = select_user(username=username, email=email)
        if self.user and check_password_hash(self.user['password'],
                                             kwargs['password']):
            message = 'Login successful'
            access_token = create_access_token(identity=self.user['username'])
            response = Response.success(message=message,
                                        access_token=access_token)
            return response, 200
        message = 'Login unsuccessful'
        info = 'Invalid username or password'
        return Response.failed(message=message, info=info), 401
