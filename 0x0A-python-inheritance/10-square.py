#!/usr/bin/python3
"""
This module defines a square with it's attributes

"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a new child class with Rectangle's attributes
    but a few changes """

    def __init__(self, size):
        """ Initializing the attributes

        Args:
            size: Size of one side

        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Defines the area of a square

        Returns:
            The area

        """

        return (self.__size * self.__size)
