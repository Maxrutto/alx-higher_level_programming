#!/usr/bin/python3
""" This module creates a class Rectangle
    and handles it's attributes

"""
class Rectangle:
    """Defines a class called Rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializing the attributes

        Args:
           width: Rectangle's width
           height: Rectangle's height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns the width

        Returns:
            rectangle width

        """

        return self.__width
    @width.setter
    def width(self, value):
        """Method that sets the value of the width

        Args:
            value: width value
        
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0

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
            The height of the rectangle

        """

        return self.__height

    @height.setter
    def height(self, value):
        """Method that defines the height of the rectangle

        Args:
            value: Height value

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the area of the rectangle

        Returns:
            Area = height * width
        """

        return self.height * self.width

    def perimeter(self):
        """Method that returns the perimeter of the rectangle

        Returns:
            Perimeter = (2 * height) + (2 * width)

        """
        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        """Method that returns the rectangle

        Returns:
            str of the rectangle in '#' form
        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"
                
            
        return rectangle[:-1]
