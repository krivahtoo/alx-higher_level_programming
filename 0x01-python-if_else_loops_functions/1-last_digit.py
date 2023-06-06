#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if (number < 0):
    last = -last

msg = "less than 6 and not 0"
if (last > 5):
    msg = "greater than 5"
elif (last == 0):
    msg = "0"

print(f"Last digit of {number:d} is {last:d} and is {msg}")
