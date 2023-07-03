#!/usr/bin/python3

"""
6. Coordinates of a square
Write a class Square that defines a square by: (based on 5-square.py)
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

    def __init__(self, size=0, position=(0, 0)) -> None:
        self.size = size
        self.position = position

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
        else:
            for y in range(self.size + self.position[1]):
                if y >= self.position[1]:
                    for x in range(self.size + self.position[0]):
                        if x >= self.position[0]:
                            print("#", end="")
                        else:
                            print(" ", end="")
                print()

    @property
    def position(self):
        """
        position getter

        Returns:
            int: the size of the square
        """
        return self.__position

    @position.setter
    def position(self, value=(0, 0)):
        """
        position setter

        Args:
            value (tuple): tuple of 2 positive integers
        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if type(value) != tuple or len(value) != 2 or\
                type(value[0]) != int or type(value[1]) != int or\
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = (value[0], value[1])


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
