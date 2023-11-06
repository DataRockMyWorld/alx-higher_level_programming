#!/usr/bin/python3
"""
This module determines if the object is an instance of a class 
that inherited (directly or indirectly) from the specified class 
"""


def inherits_from(obj, a_class):
    """
    If object is an instance of a class that iherited directly or indirectly

    Args: obj, a_class

    Return: True or False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
