#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """ This function defines a list of attributes and methods
    of an object

    Args:
        obj: The current object being listed


    Returns:
        The list of attributes and methods
    """

    return (dir(obj))
