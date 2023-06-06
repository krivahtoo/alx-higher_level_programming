#!/usr/bin/python3

def uppercase(str):
    final = ""
    for c in str:
        n = ord(c)
        if (n > 96 and n < 123):
            final += chr(n - 32)
        else:
            final += chr(n)
    print("{}".format(final))


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
