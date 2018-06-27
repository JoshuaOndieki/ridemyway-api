from ridemyway.models.request import Request
from flask import current_app as app
import re
from ridemyway.utils.validators import date_has_passed


class RequestController():
    """
        Controls all CRUD operations of the Request object.
    """

    def create_request(self, **Kwargs):
        """
            Creates and adds a request to the app database.

            Returns:
                A success status if success adding ride,
                failed status otherwise.
        """
        try:
            app.database['Rides'][Kwargs['ride_id']]
            request_ids = [x for x in app.database['Requests']]
            if request_ids:
                request_id = max(request_ids) + 1
            else:
                request_id = 1
            self.new_request = Request(
                request_id=request_id,
                ride_id=Kwargs['ride_id'],
                status='available'
                )
            request = self.new_request.__dict__
            app.database['Requests'][request['request_id']] = request
            status = {
                'status': 'success',
                'message': 'Ride request created successfully',
                'attributes': {
                    'location':
                    '/api/v1/rides/' + str(request['ride_id']) + '/requests'
                    }
                }
            return status, 201
        except KeyError:
            error_message_404 = 'Chapter 404: The Lost Resource. \
            A careful and diligent search \
            has been made for the desired resource, \
            but it just cannot be found.'
            status = {
                'status': 'failed',
                'message': 'NOT FOUND',
                'meta': {
                    'errors': 1
                    },
                'errors': [
                    {
                        404: re.sub(' +', ' ', error_message_404)
                        }
                    ]
                }
            return status, 404
