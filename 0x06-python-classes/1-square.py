#!/usr/bin/python3

"""
1. Square with size
Write a class Square that defines a square by: (based on 0-square.py)
"""


class Square:
    """
    defines a square

    Args:
        size (int): size of the square
    """

    def __init__(self, size) -> None:
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
