"""
    Testing datasets for API v2
"""

VALID_DRIVER = {
    'username': 'driver',
    'name': 'Issa Driver',
    'gender': 'male',
    'usertype': 'driver',
    'contacts': 254700000000,
    'email': 'driver@email.com',
    'password': 'pas@driver'
}

VALID_DRIVER_1 = {
    'username': 'driver1',
    'name': 'Issa Driver1',
    'gender': 'female',
    'usertype': 'driver',
    'contacts': 254700000001,
    'email': 'driver1@email.com',
    'password': 'pas@driver'
}

VALID_RIDER = {
    'username': 'rider',
    'name': 'Issa Rider',
    'gender': 'female',
    'usertype': 'rider',
    'contacts': 254710000000,
    'email': 'rider@email.com',
    'password': 'pas@rider'
}

SPECIAL_CHARS_USERNAME = {
    'username': 'ri/der',
    'name': 'Issa Rider',
    'gender': 'female',
    'usertype': 'rider',
    'contacts': 254710000000,
    'email': 'rider@email.com',
    'password': 'pas@rider'
}

SPECIAL_CHARS_NAME = {
    'username': 'rider',
    'name': 'Issa $ Rider',
    'gender': 'female',
    'usertype': 'rider',
    'contacts': 254710000000,
    'email': 'rider@email.com',
    'password': 'pas@rider'
}

INVALID_EMAIL = {
    'username': 'driver',
    'name': 'Issa Driver',
    'gender': 'male',
    'usertype': 'driver',
    'contacts': 254700000000,
    'email': 'whatsemail?',
    'password': 'pas@rider'
}

INVALID_CONTACTS = {
    'username': 'driver',
    'name': 'Issa Driver',
    'gender': 'male',
    'usertype': 'driver',
    'contacts': 'no calls!',
    'email': 'driver@email.com',
    'password': 'pas@rider'
}

INVALID_USERTYPE = {
    'username': 'driver',
    'name': 'Issa Driver',
    'gender': 'male',
    'usertype': 'user',
    'contacts': 254700000000,
    'email': 'driver@email.com',
    'password': 'pas@rider'
}

INVALID_GENDER = {
    'username': 'driver',
    'name': 'Issa Driver',
    'gender': 'both',
    'usertype': 'driver',
    'contacts': 254700000000,
    'email': 'driver@email.com',
    'password': 'pas@rider'
}

VALID_RIDE = {
    'departure': '08/01/2100 08:00AM',
    'cost': 50000,
    'vehicle': 'KDF-A21',
    'origin': 'Umoja',
    'destination': 'Andela',
    'available_capacity': 3,
    'notes': 'Some Notes here'
}

INVALID_RIDE_DATE = {
    'departure': 'not a date',
    'cost': 50000,
    'vehicle': 'KDF-A21',
    'origin': 'Umoja',
    'destination': 'Andela',
    'available_capacity': 3,
    'notes': 'Some Notes here'
}

PAST_RIDE_DATE = {
    'departure': '01/01/2018 12:00AM',
    'cost': 50000,
    'vehicle': 'KDF-A21',
    'origin': 'Umoja',
    'destination': 'Andela',
    'available_capacity': 3,
    'notes': 'Some Notes here'
}

INVALID_RIDE_COST = {
    'departure': '08/01/2100 08:00AM',
    'cost': 'hundred',
    'vehicle': 'KDF-A21',
    'origin': 'Umoja',
    'destination': 'Andela',
    'available_capacity': 3,
    'notes': 'Some Notes here'
}

INVALID_RIDE_CAPACITY = {
    'departure': '08/01/2100 08:00AM',
    'cost': 50000,
    'vehicle': 'KDF-A21',
    'origin': 'Umoja',
    'destination': 'Andela',
    'available_capacity': 3.1,
    'notes': 'Some Notes here'
}

GREATER_RIDE_CAPACITY = {
    'departure': '08/01/2100 08:00AM',
    'cost': 50000,
    'vehicle': 'KDF-A21',
    'origin': 'Umoja',
    'destination': 'Andela',
    'available_capacity': 6,
    'notes': 'Some Notes here'
}

VALID_VEHICLE = {
    'model': 'Model1',
    'number_plate': 'KDF-A12',
    'type': 'TypeA',
    'color': 'Color Y',
    'capacity': 4
}
