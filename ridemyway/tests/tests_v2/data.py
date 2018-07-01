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
    'departure': '08/01/2018 08:00AM',
    'cost': 50000,
    'vehicle': 'KDF-A21',
    'origin': 'Umoja',
    'destination': 'Andela',
    'available_capacity': 3,
    'notes': 'Some Notes here'
}
