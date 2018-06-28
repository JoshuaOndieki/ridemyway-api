"""
    Handles formatting of http responses
"""

# Default errors
ERRORS = {
    'NotFound': {
        'message': 'Chapter 404: The Lost Resource. A careful and diligent ' +
                   'search has been made for the desired resource, ' +
                   'but it just cannot be found.',
        'status': 404,
        'info': 'Visit the API Docs to see available endpoints'
    },
    'InternalServerError': {
        'message': 'Sorry about this. It\'s not you, it\'s us. ' +
                   'We just couldn\'t handle your request',
        'status': 500,
        'info': 'Please try again. If this persists, let us know'
        }
}


class Response():
    """
        Has methods for populating response templates with dynamic data
        and returns it
    """

    @staticmethod
    def success(**kwargs):
        """
            Args:
                dynamic success data
            Returns:
                Populated success template
        """
        success_response = {
            'status': 'success',
            'meta': {},
            'message': '',
            }
        for item in kwargs:
            success_response[item] = kwargs[item]
        return success_response

    @staticmethod
    def failed(**kwargs):
        """
            Args:
                dynamic errors
            Returns:
                Populated fail template
        """
        fail_response = {
            'status': 'failed',
            'message': '',
            'meta': {}
            }
        for item in kwargs:
            fail_response[item] = kwargs[item]
        return fail_response
