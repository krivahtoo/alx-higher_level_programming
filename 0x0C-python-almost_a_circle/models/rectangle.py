#!/usr/bin/python3
"""2. First Rectangle
Write the class Rectangle that inherits from Base
"""
from .base import Base


class Rectangle(Base):
    """This class inherits from the base class"""
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
        for y in range(self.height + self.y):
            if y >= self.y:
                for x in range(self.width + self.x):
                    if x >= self.x:
                        print("#", end="")
                    else:
                        print(" ", end="")
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

    def update(self, *args, **kwargs):
        """update values"""
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
