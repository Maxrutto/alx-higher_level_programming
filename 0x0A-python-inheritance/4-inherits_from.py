#!/usr/bin/python3
"""
This module defines a function that returns true if
an object is an instance of an inherited class

"""


def inherits_from(obj, a_class):
    """ Definition of the function

    Args:
        obj: The object being checked
        a_class: The base class being inherited

    Returns:
        True: if the object is an instance of the specified
        False: Otherwise


    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
