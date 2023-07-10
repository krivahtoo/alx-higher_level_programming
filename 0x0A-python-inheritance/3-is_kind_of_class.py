#!/usr/bin/python3
"""Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj: int, a_class):
    """returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class ;
    otherwise False.
    """
    if issubclass(type(obj), a_class):
        return True
    return False


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
