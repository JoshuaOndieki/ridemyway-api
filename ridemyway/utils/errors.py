"""
    Module for checking errors
"""
from .validators import (is_a_date, date_has_passed, is_number, is_int,
                         is_alphanumeric, is_email, is_gender, is_usertype,
                         is_name)
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
    elif not is_a_date(kwargs['departure']):
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


def signup_errors(**kwargs):
    message = 'Could not add user'
    errors = {}
    if not is_alphanumeric(kwargs['username']):
        errors['username'] = 'Username should only be alphanumeric.'
    if not is_name(kwargs['name']):
        errors['name'] = 'Name should only have alphabets and spaces.'
    if not is_email(kwargs['email']):
        errors['email'] = 'Invalid email provided'
    if not is_int(kwargs['contacts']):
        errors['contacts'] = 'Contacts should be a number'
    if not is_gender(kwargs['gender']):
        errors['gender'] = 'Invalid gender provided'
    if not is_usertype(kwargs['usertype']):
        errors['usertype'] = 'Usertype not known. Opt either driver | rider'
    meta = {'errors': len(errors)}
    if errors:
        return Response.failed(meta=meta, message=message, errors=errors)


def login_errors(**kwargs):
    message = 'Login unsuccessful'
    errors = {}
    if 'username' not in kwargs and 'email' not in kwargs:
        errors['identity'] = 'Provide either an email or username to login'
    if 'password' not in kwargs:
        errors['password'] = 'This field cannot be blank'
    meta = {'errors': len(errors)}
    if errors:
        return Response.failed(meta=meta, message=message, errors=errors)
