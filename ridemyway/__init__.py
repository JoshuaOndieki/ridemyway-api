"""
    App factory module
"""


from flask import Flask

from config import config
from .api.v1.routes import v1


# An in memory database
DATABASE = {"Users": {}, "Rides": {}, "Requests": {}}

"""
    ---------------------- DATA STRUCTURE -----------------
    {
        Users:
            {
                username: {name, gender, age, usertype, date_joined, contacts,
                email, password}
                            ...
            }

        Rides:
            {
                ride_id: {dateoffered, departure, driver, contribution,
                vehicle_number_plate, capacity, availability}
                            ...
            }

        Requests:
            {
                request_id: {passenger, ride_id, status}
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
    app.database = DATABASE
    app.config.from_object(config[config_name])
    app.config['BUNDLE_ERRORS'] = True

    @app.before_request
    def before_request():
        app.conn = app.config['DB_CONN']

    @app.teardown_request
    def teardown_request(exception):
        app.conn.close()

    @app.route('/')
    def api_docs():
        """ Route to the api docs"""
        from flask import render_template
        return render_template('api.html')
    # Register Blueprint here
    app.register_blueprint(v1, url_prefix="/api/v1")

    return app
