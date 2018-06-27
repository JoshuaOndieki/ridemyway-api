"""
    Controller for endpoints on rides
"""

from ridemyway.models.ride import Ride
from datetime import datetime
from flask import current_app as app
import re
from ridemyway.utils.validators import date_has_passed


class RideController():
    """
        Controls all CRUD operations of the Ride object.
    """

    def create_ride(self, **kwargs):
        """
            Creates and adds a ride to the app database.

            Returns:
                A success status if success adding ride,
                failed status otherwise.
        """
        try:
            ride_ids = [x for x in app.database['Rides']]
            if ride_ids:
                ride_id = max(ride_ids) + 1
            else:
                ride_id = 1
            date_offered = datetime.now().strftime('%b %d %Y %H:%M%p')
            self.new_ride = Ride(
                                ride_id=ride_id,
                                departure=kwargs['departure'],
                                origin=kwargs['origin'],
                                destination=kwargs['destination'],
                                vehicle_number_plate=
                                kwargs['vehicle_number_plate'],
                                capacity=kwargs['capacity'],
                                cost=kwargs['cost'],
                                date_offered=date_offered,
                                availability='available')
            ride = self.new_ride.__dict__
            app.database['Rides'][self.new_ride.ride_id] = ride
            status = {
                  'status': 'success',
                  'message': 'Ride created successfully',
                  'attributes': {
                      'location':
                      '/api/v1/rides/' + str(ride['ride_id']),
                      'repr':
                      str(ride['ride_id']) + ' - from ' +
                      ride['origin'] + ' to ' +
                      ride['destination']
                      }
                }
            return(status)
        except Exception as e:
            status = {
                'status': 'failed',
                'message': 'Exceptions',
                'meta': {
                    'errors': 1
                    },
                'errors': [
                    {
                        str(type(e)): str(e)
                        }
                    ]
                }
            return(status)

    def fetch_one(self, ride_id):
        """
            Fetches a single ride from the app database.

            Returns:
                The requested ride,
                failed status if no such ride exists.
        """
        try:
            one_ride = app.database['Rides'][ride_id]
            fetched_ride = {
                'status': 'success',
                'message': 'Ride fetched successfully',
                'data': {
                    'rideId': one_ride['ride_id'],
                    'departure': one_ride['departure'],
                    'origin': one_ride['origin'],
                    'destination': one_ride['destination'],
                    'cost': one_ride['cost'],
                    'vehicleNumberPlate': one_ride['vehicle_number_plate'],
                    'capacity': one_ride['capacity'],
                    'dateoffered': one_ride['date_offered']
                    }
                }
            return fetched_ride, 200
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

    def fetch_all(self):
        """
            Fetches all available rides from the app database.

            Returns:
                All available rides,
        """
        rides_count = 0
        fetched_rides = {
            'status': 'success',
            'message': 'Rides fetched successfully',
            'meta': {
                'rides': 0
                },
            'data': {}
            }
        for key, value in app.database['Rides'].items():
            if date_has_passed(value['departure']):
                continue
            rides_count += 1
            fetched_rides['data'][key] = {
                'departure': value['departure'],
                'origin': value['origin'],
                'destination': value['destination'],
                'cost': value['cost'],
                'vehicle_number_plate': value['vehicle_number_plate'],
                'capacity': value['capacity'],
                'dateoffered': value['date_offered']
                }
        fetched_rides['meta']['rides'] = rides_count
        return fetched_rides
