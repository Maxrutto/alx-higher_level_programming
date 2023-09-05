#!/usr/bin/python3
class Rectangle:
    """Defines a class"""
    def __init__(self, width=0, height=0):
        """Initializing variables
        
        Args:
            width: Width of the rectangle
            height: Height of the rectangle



        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method that returns value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method that defines the width
        
        Args:
            value: value of the width

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
        """Method that returns the value of the height

        Returns:
            Height of the triangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Method that defines the height

        Args:
            value: value of the height
        

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
