#!/usr/bin/python3
"""This module defines a subclass of the list class"""


class MyList(list):
    """ This class inherits the list class attributes """
    def __init__(self):
        """ Initializes variables just like the base class """
        super().__init__(self)

    def print_sorted(self):
        """Method that prints the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
