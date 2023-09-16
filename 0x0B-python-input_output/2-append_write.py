#!/usr/bin/python3
"""
This module appends to a textfile

"""


def append_write(filename="", text=""):
    """ This function appends to a text file and returns the no.
    of added characters

    Args:
        filename: The file name
        text: The text being appended

    Returns:
        The no. of characters added

    """

    with open(filename, mode='a', encoding="utf-8") as f:
        a_write = f.write(text)
        return a_write
