#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from BaseGeometry"""
    def __init__(self, width, height) -> None:
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """get the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self) -> str:
        """return Rectangle as string"""
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
