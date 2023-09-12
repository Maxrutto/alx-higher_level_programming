#!/usr/bin/python3
"""
This module validates the value in a given method

"""


class BaseGeometry:
    """ This class does not define area but validates a value """

    def area(self):
        """ This method does not define area but

        Raises:
            Exception: with message area() is not implemented

        """

        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """ Method that validates a value

        Args:
            name (str): The name of the parameter
            value (int): The parameter to validate

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.


        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
