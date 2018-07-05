"""
    JWT ID blacklist checker
"""
from flask import current_app as app


@app.jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    """
        Checks whether the identity of the token is blacklisted
        Returns:
            True if it's blacklisted, false otherwise
    """
    with app.app_context():
        jti = decrypted_token['jti']  # JWT ID
        return jti in app.blacklist
