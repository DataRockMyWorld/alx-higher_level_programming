#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""This module inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """This is a class called Rectangle"""

    def __init__(self, width, height):
        """Instantiation step"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
