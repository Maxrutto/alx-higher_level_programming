#!/usr/bin/python3
"""
This module returns a JSON representation of an object(string)

"""
import json


def to_json_string(my_obj):
    """ Function that returns a JSON representation of an object

    Args:
        my_obj: The  object being represented

    Returns:
        The JSON representation

    """

    return json.dumps(my_obj)
