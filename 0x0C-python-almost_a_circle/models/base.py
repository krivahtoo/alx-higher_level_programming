#!/usr/bin/python3
"""1. Base class
Write the first class Base:

Create a folder named models with an empty file __init__.py inside -
with this file, the folder will become a Python package
"""


class Base:
    """This class will be the “base” of all other classes in this project.
    The goal of it is to manage id attribute in all your future classes
    and to avoid duplicating the same code (by extension, same bugs)
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
