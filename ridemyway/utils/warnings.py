"""
    Module for checking warnings
"""


def edit_warnings(**kwargs):
    message = 'Edit successful with Warnings | Some data cannot be edited after signup'
    warnings = {}
    if 'username' in kwargs:
        warnings['username'] = 'Your attempt to edit username was ignored'
    if 'usertype' in kwargs:
        warnings['usertype'] = 'Your attempt to edit usertype was ignored'
    if 'date_joined' in kwargs:
        warnings['date_joined'] = 'Your attempt to edit date joined was ignored'
    meta = {'warnings': len(warnings)}
    if warnings:
        return warnings, meta, message
