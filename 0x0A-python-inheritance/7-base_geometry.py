#!/usr/bin/python3
"""This module has a class called BaseGeometry"""


class BaseGeometry:
    """This is an empty class"""

    def area(self):
        """Area of the base Geometry undefined"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(value))
        if value <= 0:
            raise ValueError("{} must be greater than o".format(value))
