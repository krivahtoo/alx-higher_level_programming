#!/usr/bin/python3
"""Write a class BaseGeometry (based on 5-base_geometry.py)."""


class BaseGeometry():
    """ empty class """

    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
