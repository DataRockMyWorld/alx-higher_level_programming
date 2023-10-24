#!/usr/bin/python3
"""Defines a square"""


class Square:
    """
    This class defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializing the objects"""
        self.__size = size
        self.__position = position

    def __str__(self):
        self.my_print()

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

    @property
    def position(self):
        """Property to retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the attribute Position"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square"""
        return self.__size * self.__size

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for row in range(self.position[1]):
            pos += "\n"
        for _ in range(self.size):
            for col in range(self.position[0]):
                pos += " "
            for _ in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """Prints the square in position"""
        print(self.pos_print(), end="")
