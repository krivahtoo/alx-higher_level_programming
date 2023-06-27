#!/usr/bin/python3

"""
5. Printing a square
Write a class Square that defines a square by: (based on 4-square.py)
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

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if self.size == 0:
            print()
        for _ in range(self.size):
            for _ in range(self.size):
                print("#", end="")
            print()


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
