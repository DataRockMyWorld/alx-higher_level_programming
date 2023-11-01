#!/usr/bin/python3
"""
This module adds two integers

"""


def add_integer(a, b=98):
    """

    Returns the sum of two integers

    Takes Arguments a and b

    returns the sum of a and b

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
