#!/usr/bin/python3
"""This module checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Fxns determines if an object is an instance of a class

    Args: obj, a_class

    Return: True or False
    """
    if isinstance(obj, a_class):
        return True
    return False
