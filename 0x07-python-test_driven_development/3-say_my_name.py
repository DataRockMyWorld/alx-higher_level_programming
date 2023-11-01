#!/usr/bin/python3
"""Module prints out strings"""


def say_my_name(first_name, last_name=""):
    """
    Function prints at leat one name

    Args: first_name, last_name (optional)

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("first_name must be a string")

    print("{} {}".format(first_name, last_name))
