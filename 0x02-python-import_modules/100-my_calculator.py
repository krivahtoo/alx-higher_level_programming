#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, div, mul

if __name__ == "__main__":
    if (not len(argv) == 4):
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    res = 0
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    if (op == "+"):
        res = add(a, b)
    elif (op == "-"):
        res = sub(a, b)
    elif (op == "/"):
        res = div(a, b)
    elif (op == "*"):
        res = mul(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {op} {b} = {res}")
