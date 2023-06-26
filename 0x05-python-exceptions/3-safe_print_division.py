#!/usr/bin/python3

# divides 2 integers and prints the result.
def safe_print_division(a, b):
    res = None
    try:
        res = a / b
    except ZeroDivisionError:
        pass
    finally:
        print(f"Inside result: {res}")
    return res


if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
