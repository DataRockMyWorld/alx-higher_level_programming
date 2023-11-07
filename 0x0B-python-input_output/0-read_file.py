#!/usr/bin/python3
"""This module reads text from a file"""


def read_file(filename=""):
    """Function reads text from a file & prints
    to standard output
    """
    with open(filename, encoding="utf-8") as Myfile:
        print(Myfile.read(), end="")
