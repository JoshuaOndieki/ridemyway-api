"""
    Module for checking errors
"""


from .validators import is_a_date, date_has_passed, is_number, is_int


def create_ride(**kwargs):
    """
        Checks errors on create ride POST requests
    """
    response = {
        'status': 'failed',
        'message': 'Could not create ride!',
        'meta': {
            'errors': 0
            },
        'errors': {}
        }

    # Check departure date is valid
    if is_a_date(kwargs['departure']):
        if date_has_passed(kwargs['departure']):
            response['errors']['date'] = 'Date of departure is in the past'
    else:
        response['errors']['date'] = 'Date of departure is in invalid format'

    # Check cost is a valid currency value
    if not is_number(kwargs['cost']):
        response['errors']['cost'] = 'Invalid cost given'

    # Check capacity is only a number
    if is_int(kwargs['capacity']) is not True:
        response['errors']['capacity'] = 'Invalid capacity given'

    # Check number plate is not a number
    if is_number(kwargs['vehicle_number_plate']):
        response['errors']['vehicleNumberPlate'] = 'Invalid vehicle number plate given'

    response['meta']['errors'] = len(response['errors'])
    if len(response['errors']) > 0:
        return response
    return False
