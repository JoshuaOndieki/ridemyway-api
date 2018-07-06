"""
    Controller for endpoints on user
"""
from flask_jwt_extended import get_jwt_identity

from ridemyway.utils.response import Response
from ridemyway.utils.db_queries import (select_user,
                                        insert_vehicle, select_vehicle)


class VehicleController():
    """
        Registers a vehicle
    """

    def register(self, **kwargs):
        """
            register vehicle
        """
        username = get_jwt_identity()
        self.user = select_user(username)
        if self.user['usertype'] == 'driver':
            vehicle = select_vehicle(kwargs['number_plate'])
            if vehicle:
                message = 'A vehicle with that numberplate is registered'
                return Response.failed(message=message), 409
            kwargs['driver'] = self.user['username']
            reg_vehicle = insert_vehicle(**kwargs)
            if reg_vehicle:
                message = 'Vehicle registered successfully'
                return Response.success(message=message), 201
        message = 'Only drivers can register vehicles'
        return Response.failed(message=message), 403
