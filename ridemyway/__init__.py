"""
    App factory module
"""


from flask import Flask
from flask_jwt_extended import JWTManager

from config import config
from .api.v1.routes import v1


# An in memory database
DATABASE = {"Users": {}, "Rides": {}, "Requests": {}}

"""
    ---------------------- DATA STRUCTURE -----------------
    {
        Users:
            {
                username: [name, gender, age, usertype, date_joined, contacts,
                email, password]
                            ...
            }

        Rides:
            {
                rideID: [dateoffered, departure, driver, contribution,
                vehicle_number_plate, capacity, availability]
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
    app.database = DATABASE
    app.config.from_object(config[config_name])
    app.config['BUNDLE_ERRORS'] = True
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.jwt = JWTManager(app)
    app.blacklist = set()

    @app.jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        """
            Check for blacklisted tokens
        """
        jti = decrypted_token['jti']
        return jti in app.blacklist

    # Register Blueprint here
    app.register_blueprint(v1, url_prefix="/api/v1")

    return app
