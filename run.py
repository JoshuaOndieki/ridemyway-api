"""
    Runs flask server
"""
import os
from ridemyway import create_app

environment = os.getenv('FLASK_ENV')
app = create_app(environment)


if __name__ == "__main__":
    app.run()
