"""
    User model
"""
from werkzeug.security import generate_password_hash


class User():
    """
        Creates User objects.

        **kwargs:
            username: A unique alias for the users
            name: Real name of the user
            gender: Gender of the user
            usertype: driver / rider
            date_joined: Date user was registered
            contacts: User contact number
            email: email address of the user
            password: password
    """

    def __init__(self, kwargs):
        self.username = kwargs['username']
        self.name = kwargs['name']
        self.gender = kwargs['gender']
        self.usertype = kwargs['usertype']
        self.date_joined = kwargs['date_joined']
        self.contacts = int(kwargs['contacts'])
        self.email = kwargs['email']
        self.set_password(kwargs['password'])

    def set_password(self, password):
        self.password = generate_password_hash(password)
