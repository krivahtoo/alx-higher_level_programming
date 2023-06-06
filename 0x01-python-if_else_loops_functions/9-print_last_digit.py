#!/usr/bin/python3

def print_last_digit(number):
    last = abs(number) % 10
    print(f"{last}", end='')
    return last


if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
