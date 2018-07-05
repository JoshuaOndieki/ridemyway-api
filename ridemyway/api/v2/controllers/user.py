"""
    Controller for endpoints on user
"""

from ridemyway.utils.response import Response
from ridemyway.utils.db_queries import select_user


class UserController():
    """
        Gets | Edits a user.
    """

    def fetch_user(self, username):
        user = select_user(username)
        if user:
            message = 'User fetched successfully'
            attributes = {
                'location': '/api/v2/users/' + user['username']
            }
            # MAKE SURE THE PASSWORD IS POPPED BEFORE RETURNING THE USER!!!
            del user['password']
            # Now :) it's safe to return the other details
            return Response.success(message=message, attributes=attributes,
                                    data=user), 200
        message = 'No such user'
        return Response.failed(message=message), 404
