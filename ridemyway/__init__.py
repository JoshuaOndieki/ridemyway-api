from flask import Flask
from config import config
from .api.v1.routes import v1


# An in memory database
database = {"Users": {}, "Rides": {}, "Requests": {}}

"""
    ---------------------- DATA STRUCTURE -----------------
    {
        Users:
            {
                username: [name, gender, age, usertype, date_joined, contacts, email, password]
                            ...
            }

        Rides:
            {
                rideID: [dateoffered, departure, driver, contribution, vehicle_number_plate, capacity, availability]
                            ...
            }

        Requests:
            {
                requestID: [passenger, rideID, status]
                            ...
            }
    }
"""


def create_app(config_name):
    """
    Usage: Factory function used to setup the application instance
    :return: application instance
    """
    app = Flask(__name__)
    app.database = database
    app.config.from_object(config[config_name])

    app.register_blueprint(v1, url_prefix="/api/v1")
    return app
