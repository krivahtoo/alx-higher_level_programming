#!/usr/bin/python3
"""10. And now, the Square!
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """represents a square inheriting the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """covert square to string"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self) -> int:
        """get the size of the square"""
        return self.width

    @size.setter
    def size(self, size):
        """set the size of square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the square values"""
        if kwargs is not None and len(args) <= 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value
        else:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg

    def to_dictionary(self):
        """return dict representation"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
