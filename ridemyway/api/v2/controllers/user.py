"""
    Controller for endpoints on user
"""
from flask_jwt_extended import get_jwt_identity

from ridemyway.utils.response import Response
from ridemyway.utils.db_queries import select_user, update_user
from ridemyway.utils.warnings import edit_warnings


class UserController():
    """
        Gets | Edits a user.
    """

    def fetch_user(self, username):
        self.user = select_user(username)
        if self.user:
            message = 'User fetched successfully'
            attributes = {
                'location': '/api/v2/users/' + self.user['username']
            }
            # MAKE SURE THE PASSWORD IS POPPED BEFORE RETURNING THE USER!!!
            del self.user['password']
            # Now :) it's safe to return the other details
            return Response.success(message=message, attributes=attributes,
                                    data=self.user), 200
        message = 'No such user'
        return Response.failed(message=message), 404

    def edit_user(self, **kwargs):
        immutable_fields = ['username', 'usertype', 'date_joined']
        username = get_jwt_identity()
        self.warnings = edit_warnings(**kwargs)
        user = select_user(username=username)
        if 'email' in kwargs:
            user_exists = select_user(email=kwargs['email'])
            if user_exists and user_exists['username'] is not user['username']:
                message = 'Email already in use by another user'
                response = Response.failed(message=message)
                return response, 403
        for field in kwargs:
            if field not in immutable_fields:
                user[field] = kwargs[field]
        update_user(**user)
        message = 'Edit user successful'
        if self.warnings:
            message = self.warnings[2]
            meta = self.warnings[1]
            warnings = self.warnings[0]
            return Response.success(message=message, meta=meta,
                                    warnings=warnings), 201
        return Response.success(message=message), 201
