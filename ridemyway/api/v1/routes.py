"""
    Register routes for the app
"""

from flask import Blueprint
from flask_restful import Api
from ridemyway import resources as r


v1 = Blueprint('v1', __name__)
api = Api(v1)
add = api.add_resource


# Add routes here
add(r.All, '/all')                                      # GET
add(r.Rides, '/rides')                                  # GET, POST
add(r.Ride, '/rides/<int:ride_id>')                      # GET
add(r.Request, '/rides/<int:ride_id>/requests')          # POST
