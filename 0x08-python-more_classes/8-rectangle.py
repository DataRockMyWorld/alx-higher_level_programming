#!/usr/bin/python3
"""
This module contains a class called a rectangle

"""


class Rectangle:
    """
    This class defines a rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """print a message for every object that is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
