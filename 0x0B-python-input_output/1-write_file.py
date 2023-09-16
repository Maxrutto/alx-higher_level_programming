#!/usr/bin/python3
"""
This module writes a string to a text file

"""


def write_file(filename="", text=""):
    """ This function writes to a textfile

    Args:
        filename: The filename
        text: The text being written

    Returns:
        The number of characters written

    """

    with open(filename, mode='w', encoding="utf-8") as f:
        a_write = f.write(text)
        return a_write
