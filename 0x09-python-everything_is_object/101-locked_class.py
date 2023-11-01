#!/usr/bin/python3
"""Module contains a class called LockedClass"""


class LockedClass:
    """

    Class prevents user from dynamically
    creating a new instance attribute except first_name

    """

    __slots__ = "first_name"
