#!/usr/bin/python3

for ch in reversed(range(0, 26)):
    print("{}".format(
        chr(ch + ord('A')) if ch % 2 == 0 else chr(ch + ord('a'))
    ), end="")
