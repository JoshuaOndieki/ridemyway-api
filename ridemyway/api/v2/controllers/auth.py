"""
    Controller for endpoints on auth
"""

from datetime import datetime

from ridemyway.utils.response import Response
from ridemyway.utils.db_queries import sql_signup
from ridemyway.api.v2.models.user import User
from ridemyway.utils.db_queries import get_user


class AuthController():
    """
        Controls all CRUD operations of the User object.
    """

    def signup(self, **kwargs):
        """

        """
        now = datetime.now()
        kwargs['date_joined'] = now.strftime('%b %d %Y %H:%M%p')
        user = User(kwargs)
        user_exists = get_user(username=user.username, email=user.email)
        if user_exists:
            return Response.failed(message='Such user exists'), 409
        sql_signup(user)
        message = 'User created successfully'
        attributes = {
            'location': '/api/v2/users/' + user.username
        }
        return Response.success(message=message, attributes=attributes), 201
