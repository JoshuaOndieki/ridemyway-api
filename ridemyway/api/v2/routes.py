"""
    Register routes for the app
    Here's where URLs are matched to resources
"""

from flask import Blueprint
from flask_restful import Api
from . import resources as r
from ridemyway.utils.response import ERRORS


v2 = Blueprint('v2', __name__)
api = Api(v2, catch_all_404s=True, errors=ERRORS)
add = api.add_resource


# Add routes here
add(r.Signup, '/auth/signup')                                  # POST
add(r.Login, '/auth/login')                                    # POST
add(r.Logout, '/auth/logout')                                  # POST
add(r.GetUser, '/users/<username>')                            # GET
add(r.EditUser, '/users')                                      # PUT
add(r.Vehicle, '/vehicle')                                     # POST
