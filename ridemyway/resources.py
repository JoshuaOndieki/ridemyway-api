from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token,
                                create_refresh_token, jwt_required,
                                get_jwt_identity, get_raw_jwt)
from flask import current_app as app

from ridemyway.controllers.ride_controller import RideController


rides = RideController()


class Rides(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('departure',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('origin',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('destination',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('cost',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('vehicle_number_plate',
                                 help='This field cannot be blank',
                                 required=True)
        self.parser.add_argument('capacity',
                                 help='This field cannot be blank',
                                 required=True)

    def get(self):
        """
            Gets all available rides and responds with a json formatted data
        """
        data = self.parser.parse_args()
        self.response = rides.create_ride(**data)
        return self.response, 201


class All(Resource):

    def __init__(self):
        pass

    def get(self):
        """
            Returns:
                All database items
        """

        return {'message': 'all'}, 201
