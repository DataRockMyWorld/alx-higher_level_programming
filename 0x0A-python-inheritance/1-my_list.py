#!/usr/bin/python3
"""
This module consist of class Mylist
"""


class MyList(list):
    """
    Class inherits from list
    """

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
