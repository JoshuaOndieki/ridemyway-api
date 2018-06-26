from .validators import is_a_date, date_has_passed, is_currency, is_int


def create_ride(**kwargs):
    """

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
    if not is_currency(kwargs['cost']):
        response['errors']['cost'] = 'Invalid cost given'

    # Check capacity is only a number
    if is_int(kwargs['capacity']) is not True:
        response['errors']['capacity'] = 'Invalid capacity given'

    # Check number plate is a string
    try:
        float(kwargs['vehicle_number_plate'])
        response['errors']['vehicleNumberPlate'] = 'Invalid vehicle number plate given'
    except Exception:
        pass
    response['meta']['errors'] = len(response['errors'])
    if len(response['errors']) > 0:
        return response
    return False
