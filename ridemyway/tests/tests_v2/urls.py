"""
    API v2 URLs
"""

# Root url for v2 of the API
ROOT_URL = '/api/v2'

SIGNUP = ROOT_URL + '/auth/signup'
LOGIN = ROOT_URL + '/auth/login'

USER = ROOT_URL + '/users'

RIDE = ROOT_URL + '/rides'

VEHICLE = ROOT_URL + '/vehicle'

REQUEST = ROOT_URL + 'rides/<ride_id>/requests'
