#!/usr/bin/python3
"""This module defines a subclass of the list class"""


class MyList(list):
    """ This class inherits the list class attributes

    Args:
        list: class list


    """
    def __init__(self):
        """ Initializes variables just like the base class """
        super().__init__()

    def print_sorted(self):
        """Method that prints the list in ascending order"""
        print(sorted(self))
