#!/usr/bin/python3
"""
Function that adds an attribute to an object

"""


def add_attribute(obj, name, value):
    """ Method that adds an atrribute to an object obj

    Args:
        obj: The object being added to
        name: The attribute name
        value: The attribute value

    Raises:
        TypeError: If the object can't be added attributes

    """

    if hasattr(obj, '__dict__'):
        obj.__dict__[name] = value
    else:
        raise TypeError("can't add new attribute")
