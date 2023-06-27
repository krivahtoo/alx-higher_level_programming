#!/usr/bin/python3

"""
3. Area of a square
Write a class Square that defines a square by: (based on 2-square.py)
"""


class Square:
    """
    defines a square

    Args:
        size (int): size of the square
    Raises:
        TypeError: If size is not integer
        ValueError: If size < 0
    """

    def __init__(self, size=0) -> None:
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculates the current square area

        Returns:
            int: the area of the square
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
