#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    n = len(argv)
    print(f"{n-1} arguments", end="")

    if (n < 2):
        print(".")
    else:
        print(":")
    for k, v in enumerate(argv[1:]):
        print(f"{k+1}: {v}")
