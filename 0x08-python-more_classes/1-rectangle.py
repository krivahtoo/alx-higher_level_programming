#!/usr/bin/python3
"""
1. Real definition of a rectangle
Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """ defines a rectangle """
    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get this rectangle's width """
        return self.__width

    @width.setter
    def width(self, value: int):
        """
        set this rectangle's width

        Args:
            value (int): value to set
        Raises:
            TypeError: If width is not an int
            ValueError: If width is less than 0
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self) -> int:
        """ get this rectangle's height """
        return self.__height

    @height.setter
    def height(self, value: int):
        """
        set this rectangle's height

        Args:
            value (int): value to set
        Raises:
            TypeError: If height is not an int
            ValueError: If height is less than 0
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
