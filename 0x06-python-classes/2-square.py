#!/usr/bin/python3


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