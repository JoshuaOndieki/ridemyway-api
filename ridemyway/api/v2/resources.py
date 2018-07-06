"""
    v2 API resources
    Resources check for presence of required data and pass to errors
    for semantic error checks
    Clean data without semantic errors is further handled by the controllers
"""
import json
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_raw_jwt
from flask import current_app as app

from .controllers.auth import AuthController
from ridemyway.utils import errors
from ridemyway.utils.response import Response


auth = AuthController()


class Signup(Resource):
    """
        SIGNUP Resource
    """

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('name',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('gender',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('usertype',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('email',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('password',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('contacts',
                                 help='This field cannot be blank',
                                 required=True)

    def post(self):
        """
            User SIGNUP
        """
        self.data = self.parser.parse_args()
        signup_errors = errors.signup_errors(**self.data)
        if signup_errors:
            return json.loads(json.dumps(signup_errors)), 422
        return auth.signup(**self.data)


class Login(Resource):
    """
        Login Resource
    """
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('password',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('username')
        self.parser.add_argument('email')

    def post(self):
        self.data = self.parser.parse_args()
        login_errors = errors.login_errors(**self.data)
        if login_errors:
            return json.loads(json.dumps(login_errors)), 422
        return auth.login(**self.data)


class Logout(Resource):
    """
        Logs out a user and revokes the token
    """
    @jwt_required
    def post(self):
        """
            Revokes a token and blacklists it.
        """
        self.jti = get_raw_jwt()['jti']
        app.blacklist.add(self.jti)
        message = 'Log out successful'
        return Response.success(message=message)
