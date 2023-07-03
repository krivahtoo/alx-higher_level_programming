#!/usr/bin/python3

"""
9. Compare 2 squares
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
        print(self)

    def __str__(self) -> str:
        """
        return string version of Square
        """
        val = ""
        if self.size != 0:
            for y in range(self.size + self.position[1]):
                if y >= self.position[1]:
                    for x in range(self.size + self.position[0]):
                        if x >= self.position[0]:
                            val += "#"
                        else:
                            val += " "
                if y + 1 != self.size + self.position[1]:
                    val += "\n"
        return val

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

    def __le__(self, value) -> bool:
        """
        less than
        """
        return self.size < value.size

    def __gt__(self, value) -> bool:
        """
        greatter than
        """
        return self.size > value.size

    def __ge__(self, value) -> bool:
        """
        greatter than or equal
        """
        return self.size >= value.size

    def __eq__(self, value) -> bool:
        """
        equal
        """
        return self.size == value.size


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
