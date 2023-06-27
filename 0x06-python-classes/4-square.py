#!/usr/bin/python3

"""
4. Access and update private attribute
Write a class Square that defines a square by: (based on 3-square.py)
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
        self.size = size

    def area(self):
        """
        calculates the current square area

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        size getter

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        size setter

        Args:
            size (int): size of the square
        Raises:
            TypeError: If size is not integer
            ValueError: If size < 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
