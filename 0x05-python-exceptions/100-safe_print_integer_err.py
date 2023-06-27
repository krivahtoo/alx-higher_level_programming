#!/usr/bin/python3

from sys import stderr


# prints an integer.
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as e:
        print(f"Exception: {e}", file=stderr)
        return False
    return True


if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
