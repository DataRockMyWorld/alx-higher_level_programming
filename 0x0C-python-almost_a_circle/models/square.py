#!/usr/bin/python3
"""The square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class moduled after a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize objects"""
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print out class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Gets width attribute"""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Assign attribute to args"""
        attributes = ["id", "size", "x", "y"]

        if args:
            for i, value in enumerate(args):
                if attributes[i] != "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                setattr(
                    self, attributes[i], value
                ) if value is not None else self.__init__(self.size, self.x, self.y)

        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int:
                        raise TypeError("id must be an integer")
                setattr(self, key, value) if value is not None else self.__init__(
                    self.size, self.x, self.y
                )

    def to_dictionary(self):
        """Returns the dictionary representation of square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
