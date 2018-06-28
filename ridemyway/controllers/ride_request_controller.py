"""
    Controller for endpoints on ride requests
"""


from flask import current_app as app

from ridemyway.models.request import Request
from ridemyway.utils.response import Response


class RequestController():
    """
        Controls all CRUD operations of the Request object.
    """

    def create_request(self, **kwargs):
        """
            Creates and adds a request to the app database.

            Returns:
                A success status if success adding ride,
                failed status otherwise.
        """
        if kwargs['ride_id'] in app.database['Rides']:
            request_ids = [x for x in app.database['Requests']]
            if request_ids:
                request_id = max(request_ids) + 1
            else:
                request_id = 1
            self.new_request = Request(
                request_id=request_id,
                ride_id=kwargs['ride_id'],
                status='available'
                )
            request = self.new_request.__dict__
            app.database['Requests'][request['request_id']] = request
            message = 'Ride request created successfully'
            attributes = {
                'location':
                '/api/v1/rides/' + str(request['ride_id']) + '/requests'
                }
            response = Response.success(message=message, attributes=attributes)
            return response, 201
        meta = {'errors': 1,
                'source': '/' + str(kwargs['ride_id']) + '/requests'}
        message = 'NOT FOUND'
        info = 'The ride you requested does not exist'
        response = Response.failed(meta=meta,
                                   message=message,
                                   info=info)
        return response, 404
