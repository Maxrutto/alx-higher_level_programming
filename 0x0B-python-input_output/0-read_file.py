#!/usr/bin/python3
"""
This module reads a file and prints it to stdout

"""


def read_file(filename=""):
    """ This function reads a text file and prints it

    Args:
        filename: The name of the file

    """

    with open(filename, encoding="utf-8") as f:
        a_read = f.read()
        print(a_read, end='')
