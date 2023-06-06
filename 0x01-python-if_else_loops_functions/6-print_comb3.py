#!/usr/bin/python3

for y in range(0, 8):
    for x in range(0, 10):
        if (x > y):
            print("{0:d}{1:d}, ".format(y, x), end='')
print("{}".format(89))
