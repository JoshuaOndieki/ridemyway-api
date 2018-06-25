from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token,
                                create_refresh_token, jwt_required,
                                get_jwt_identity, get_raw_jwt)
from flask import current_app as app


class All(Resource):

    def __init__(self):
        pass

    def get(self):
        """
            Returns:
                All database items
        """
        
        return {'message': 'all'}, 201
