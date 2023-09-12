#!/usr/bin/python3
"""
Defines a class MyInt that inherits int

"""


class MyInt(int):
    """ Inverts int operators == and != """

    def __eq__(self, value):
        """ Override the == operator with != behavior

        Returns:
            The inverted operator

        """

        return self.real != value

    def __ne__(self, value):
        """ Override != operator with == behavior

        Returns:
            The inverted operator

        """

        return self.real == value
