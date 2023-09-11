#!/usr/bin/python3
"""
This module checks if an object is an instance

"""


def is_same_class(obj, a_class):
    """ Defines a function

    Args:
        obj: Object to be checked
        a_class: The class of the object

    Returns:
        True: if obj is exactly an instance of a_class
        False: if not

    """

    if type(obj) == a_class:
        return (True)
    else:
        return (False)
