#!/usr/bin/python3
"""
3. Print square
Write a function that prints a square with the character #.
"""


def print_square(size):
    """ prints a square with the character # """
    if type(size) != int and (type(size) == float and size <= 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()


if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
