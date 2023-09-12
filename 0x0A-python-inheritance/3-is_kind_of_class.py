#!/usr/bin/python3
"""
This module checks if the object is kind of a clas instance

"""


def is_kind_of_class(obj, a_class):
    """ This function checks if obj is an instance of a_class or path to
    instance of a_class

    Args:
        obj: The object being checked
        a_class: The class or super class

    Returns:
        True: if obj is instance or is an instance of an instance
        False: if none of the above

    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
