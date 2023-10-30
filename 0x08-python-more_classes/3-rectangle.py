#!/usr/bin/python3
"""
This module contains a class called a rectangle

"""


class Rectangle:
    """
    This class defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve the width of the object"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the width of the object"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the object"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting the height of the object"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        The area of the rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        P = 2 * (self.__height + self.__width)
        return P

    def __str__(self):
        """Print a rectangle of rectangles"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height):
            rec += self.__width * "#"
            if i != self.__height - 1:
                rec += "\n"
        return rec
