#!/usr/bin/python3
"""2. First Rectangle
Write the class Rectangle that inherits from Base
"""
from .base import Base


class Rectangle(Base):
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get Rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set Rectangle width"""
        self.__validate("width", width)
        self.__width = width

    @property
    def height(self):
        """get rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set rectangle height"""
        self.__validate("height", height)
        self.__height = height

    @property
    def x(self):
        """get rectangle x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set rectangle x"""
        self.__validate("x", x, True)
        self.__x = x

    @property
    def y(self):
        """get rectangle y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set rectangle y"""
        self.__validate("y", y, True)
        self.__y = y

    def __validate(self, name, x, zero=False):
        """validate integer value"""
        if type(x) != int:
            raise TypeError(f"{name} must be an integer")
        if zero:
            if x < 0:
                raise ValueError(f"{name} must be >= 0")
        else:
            if x <= 0:
                raise ValueError(f"{name} must be > 0")

    def area(self):
        """calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print current rectangle"""
        for _ in range(self.height):
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self) -> str:
        """return rectangle as string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
        )
