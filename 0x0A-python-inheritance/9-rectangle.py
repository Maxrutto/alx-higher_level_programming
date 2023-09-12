#!/usr/bin/python3
"""
Defines a child class that inherits a base class

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Child class that inherits BaseGeometry's attributes """
    def __init__(self, width, height):
        """ Initializing the variables

        Args:
            width: The width of the Rectangle
            height: The height of the Rectangle

        """

        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Implements the area

        Returns:
            The area

        """

        return (self.__width * self.__height)

    def __str__(self):
        """ The magic method for string representation

        Returns:
            A string

        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
