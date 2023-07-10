#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a squre class inheriting rectangle class"""
    def __init__(self, size) -> None:
        self.integer_validator("size", size)
        super().__init__(size, size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
