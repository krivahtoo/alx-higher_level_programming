#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r") as fd:
        for line in fd.readlines():
            print(line, end="")


if __name__ == "__main__":
    read_file("my_file_0.txt")
