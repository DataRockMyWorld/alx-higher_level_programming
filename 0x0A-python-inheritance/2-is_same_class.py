#!/usr/bin/python3
"""This module checks if an object is an exact instance of a class"""


def is_same_class(obj, a_class):
    """
    Fxns determines if an object is an exact instance of a class

    Args: obj, a_class

    Return: True or False
    """
    return type(obj) == a_class
