"""
    BASE testing module
"""
from ridemyway.tests import BaseTest


class V1BaseTest(BaseTest):
    """
        v1 Base class for testing
    """
    def setUp(self):
        """
            Set up tests
        """
        super().setUp()
        self.context.push()


# TEST DATA
VALID_RIDE_DATASET = {
    'departure': 'Jun 25 2050  1:30PM',
    'origin': 'Nairobi',
    'destination': 'Garissa',
    'cost': 350,
    'vehicle_number_plate': 'KBC-A21',
    'capacity': 3}
VALID_RIDE_DATASET_1 = {
    'departure': 'Jun 28 2050  7:00AM',
    'origin': 'Garissa',
    'destination': 'Nairobi',
    'cost': 500,
    'vehicle_number_plate': 'KBC-A21',
    'capacity': 3}
INVALID_DATE_DATASET = {
    'departure': 'Not a date',
    'origin': 'Nairobi',
    'destination': 'Garissa',
    'cost': 350, 'vehicle_number_plate':
    'KBC-A21', 'capacity': 3
    }
PAST_DATE_DATASET = {
    'departure': 'Jun 25 1901  1:30PM',
    'origin': 'Nairobi',
    'destination': 'Garissa',
    'cost': 350, 'vehicle_number_plate':
    'KBC-A21', 'capacity': 3
    }
INVALID_COST_DATASET = {
    'departure': 'Jun 25 2018  1:30PM',
    'origin': 'Nairobi',
    'destination': 'Garissa',
    'cost': '%^$', 'vehicle_number_plate':
    'KBC-A21', 'capacity': 3
    }
INVALID_CAPACITY_DATASET = {
    'departure': 'Jun 25 2018  1:30PM',
    'origin': 'Nairobi',
    'destination': 'Garissa',
    'cost': 350, 'vehicle_number_plate':
    'KBC-A21', 'capacity': 3.5
    }
INVALID_VEHICLE_NUMBER_PLATE = {
    'departure': 'Jun 25 2018  1:30PM',
    'origin': 'Nairobi',
    'destination': 'Garissa',
    'cost': 350, 'vehicle_number_plate':
    2121, 'capacity': 3
    }
