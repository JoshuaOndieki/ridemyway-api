class Ride():
    """
        Creates Ride objects.

        **Kwargs:
            ride_id: A unique identifier for the ride.
            departure: Date and time the ride is to take place.
            origin: Place where the ride starts.
            destination: Where the ride should end.
            vehicle_number_plate: The number plate of the vehicle.
            capacity: Maximum number of passengers the ride will accept.
            cost: The cost of receiving the ride.
            date_offered: The time this ride offer was created.
            availability: Status of the ride.
    """

    def __init__(self, **kwargs):
        """
            Ride object initializer.

            Returns:
                Object
        """
        self.ride_id = kwargs['ride_id']
        self.departure = kwargs['departure']
        self.origin = kwargs['origin']
        self.destination = kwargs['destination']
        self.vehicle_number_plate = kwargs['vehicle_number_plate']
        self.capacity = kwargs['capacity']
        self.cost = kwargs['cost']
        self.date_offered = kwargs['date_offered']
        self.availability = kwargs['availability']

    def __repr__(self):
        return(self.ride_id + ' - from ' +
               self.origin + ' to ' + self.destination)
