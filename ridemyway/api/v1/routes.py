from flask import Blueprint
from flask_restful import Api
from ridemyway import resources as r


v1 = Blueprint('v1', __name__)
api = Api(v1)
add = api.add_resource
