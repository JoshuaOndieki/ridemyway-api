"""
    Validates given args with defined formats and conditions
"""

import re
from datetime import datetime


def is_a_date(date_text):
    """
        Returns true if date_text is a date
        False otherwise
    """
    try:
        datetime.strptime(date_text, '%b %d %Y %I:%M%p')
        return True
    except ValueError:
        return False


def date_has_passed(date_text):
    """
        Returns true if date_text is a date that has passed
        False otherwise
    """
    date = datetime.strptime(date_text, '%b %d %Y %I:%M%p')
    if date < datetime.now():
        return True
    return False


def is_number(number):
    """
        Returns true if number is a valid number value
        False otherwise
    """
    try:
        float(number)
        return True
    except (ValueError, TypeError):
        return False


def is_int(number):
    """
        Returns true if number is an integer
        False otherwise
    """
    try:
        int(number)
        return True
    except (ValueError, TypeError):
        return False


def is_alphanumeric(string):
    """
        Checks whether a string is is alphanumeric. No special chars
    """
    return re.match('^[a-zA-Z0-9]+$', string)


def is_name(string):
    """
        Name should only have alphabets and spaces
    """
    return re.match('^[a-zA-Z ]*$', string)


def is_email(email):
    """
        Checks whether argument given is a valid email
    """
    return re.match('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
                    email)


def is_gender(gender):
    """
        Check whether argument given is a valid gender type
        Male | Female
    """
    if gender.lower() in ['male', 'female']:
        return True


def is_usertype(usertype):
    """
        Checks the usertype is valid
        driver | rider
    """
    if usertype.lower() in ['driver', 'rider']:
        return True
