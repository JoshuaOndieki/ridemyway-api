from flask import Flask
from config import config
from .api.v1.routes import v1
from flask_jwt_extended import JWTManager


# An in memory database
database = {"Users": {}, "Rides": {}, "Requests": {}}

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
    app = Flask(__name__, template_folder='../api_docs')
    app.database = database
    app.config.from_object(config[config_name])
    app.config['BUNDLE_ERRORS'] = True
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    app.config['JWT_BLACKLIST_ENABLED'] = True
    app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
    app.jwt = JWTManager(app)
    app.blacklist = set()

    @app.jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in app.blacklist

    @app.route('/')
    def api_docs():
        """ Route to the api docs"""
        from flask import render_template
        return render_template('api.html')
    # Register Blueprint here
    app.register_blueprint(v1, url_prefix="/api/v1")

    return app
