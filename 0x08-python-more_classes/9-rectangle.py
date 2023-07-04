#!/usr/bin/python3
"""
9. A square is a rectangle
Write a class Rectangle that defines a rectangle by: (based on 8-rectangle.py)
"""


class Rectangle:
    """ defines a rectangle """
    number_of_instances: int = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    val += str(self.print_symbol)
                if i + 1 != self.height:
                    val += "\n"
        return val

    def __repr__(self) -> str:
        """
        return a string representation of the rectangle to be able to
        recreate a new instance by using eval()
        """
        return "Rectangle({},{})".format(self.width, self.height)

    def __del__(self):
        """ detect deletion """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns the biggest rectangle based on the area
        """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)


if __name__ == "__main__":
    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(
        my_square.area(),
        my_square.perimeter()
    ))
    print(my_square)
