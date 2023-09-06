#!/usr/bin/python3
"""Defining a class called Rectangle"""

class Rectangle:
    """ Defining the class"""

    def __init__(self, width=0, height=0):
        """Initializing variables

        Args:
            width: The width
            height: The height

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns the width

        Returns: width

        """

        return self.__width

    @width.setter
    def width(self, value):
        """Method that defines the width

        Args:
            value: width
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """Method that returns the height
        Returns:
            Height
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Method that defines the height

        Args:
            value: height of the rectangle
        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Method that returns the rectangle area
        Returns:
            Area of the rectangle
        
        """
        
        return self.width * self.height

    def perimeter(self):
        """Method that returns the rectangle perimeter
        Returns:
            Perimeter of the rectangle

        """
        
        if self.width == 0 or self.height == 0:
            return 0
        
        return (2 * self.height) + (2 * self.width)
