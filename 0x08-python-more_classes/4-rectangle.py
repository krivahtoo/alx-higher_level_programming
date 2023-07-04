#!/usr/bin/python3
"""
4. Eval is magic
Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
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

    def area(self):
        """
        calculates the rectangle area
        """
        return self.height * self.width

    def perimeter(self):
        """
        calculates the rectangle perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self) -> str:
        """
        returns formatted string representation
        """
        val = ""
        if self.height != 0 and self.width != 0:
            for i in range(self.height):
                for _ in range(self.width):
                    val += "#"
                if i + 1 != self.height:
                    val += "\n"
        return val

    def __repr__(self) -> str:
        """
        return a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({},{})".format(self.width, self.height)


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
