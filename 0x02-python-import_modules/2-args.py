#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    n = len(argv)
    print(f"{n-1} argument", end="")

    if (not n == 2):
        print("s", end="")
    if (n < 2):
        print(".")
    else:
        print(":")
    for k, v in enumerate(argv[1:]):
        print(f"{k+1}: {v}")
