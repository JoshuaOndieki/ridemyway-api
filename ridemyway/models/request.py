class Request():
    """
        Creates Request objects.

        **kwargs:
            ride_id: A unique identifier of the ride the request is
                    being made to.
            request_id: A unique identifier for the request.
            status: Status of the request.
    """

    def __init__(self, **kwargs):
        """
            Request object initializer.

            Returns:
                Object
        """
        self.request_id = kwargs['request_id']
        self.ride_id = kwargs['ride_id']
        self.status = kwargs['status']
