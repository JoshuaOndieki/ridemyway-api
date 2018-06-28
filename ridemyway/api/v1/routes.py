"""
    Register routes for the app
"""

from flask import Blueprint
from flask_restful import Api
from . import resources as r
from ridemyway.utils.response import ERRORS


v1 = Blueprint('v1', __name__)
api = Api(v1, catch_all_404s=True, errors=ERRORS)
add = api.add_resource


# Add routes here
add(r.All, '/all')                                      # GET
add(r.Rides, '/rides')                                  # GET, POST
add(r.Ride, '/rides/<int:ride_id>')                      # GET
add(r.Request, '/rides/<int:ride_id>/requests')          # POST
