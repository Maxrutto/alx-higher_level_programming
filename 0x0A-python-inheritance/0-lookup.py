#!/usr/bin/python3
def lookup(obj):
    """ This function defines a list of attributes and methods
    of an object

    Args:
        obj: The current object being listed from


    Returns:
        The list of attributes and methods
    """
    
    return dir(obj)
