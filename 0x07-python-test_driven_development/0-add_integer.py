#!/usr/bin/python3
"""

This module is composed by a function that adds two numbers

"""

def add_integer(a, b=98):
    """ This function implements addition
        Args:
            a: The first number
            b: The second number

        Raises:
            TypeError: If any of the numbers are not
            integers or float types

        Returns:
            Addition
    
    """
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a+b)
