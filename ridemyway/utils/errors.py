"""
    Module for checking errors
"""


from .validators import is_a_date, date_has_passed, is_number, is_int
from .response import Response


def create_ride(**kwargs):
    """
        Checks errors on create ride POST requests
    """
    message = 'Could not create ride!'
    errors = {}

    # Check departure date is valid
    if is_a_date(kwargs['departure']) and date_has_passed(kwargs['departure']):
        errors['date'] = 'Date of departure is in the past'
    else:
        errors['date'] = 'Date of departure is in invalid format'

    # Check cost is a valid currency value
    if not is_number(kwargs['cost']):
        errors['cost'] = 'Invalid cost given'

    # Check capacity is only a number
    if not is_int(kwargs['capacity']):
        errors['capacity'] = 'Invalid capacity given'

    # Check number plate is not a number
    if is_number(kwargs['vehicle_number_plate']):
        errors['vehicleNumberPlate'] = 'Invalid vehicle number plate given'

    meta = {'errors': len(errors)}
    if errors:
        return Response.failed(meta=meta, message=message, errors=errors)
    return False
