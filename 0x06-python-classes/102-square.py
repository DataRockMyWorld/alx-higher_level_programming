#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    This class defines a square.
    """

    def __init__(self, size=0):
        """
        Initializing the objects
        """
        if not isinstance(size, int):
            raise TypeError("size must be >= 0")

        if size < 0:
            raise ValueError("size must be an integer")

        self.__size = size

    @property
    def size(self):
        """Property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the attribute size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculate the area of the square
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
