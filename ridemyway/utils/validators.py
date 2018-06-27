"""
    Validates given args with defined formats and conditions
"""


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
    except ValueError or TypeError:
        return False


def is_int(number):
    """
        Returns true if number is an integer
        False otherwise
    """
    try:
        int(number)
        return True
    except ValueError or TypeError:
        return False
