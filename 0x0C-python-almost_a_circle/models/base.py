#!/usr/bin/python3
"""1. Base class
Write the first class Base:

Create a folder named models with an empty file __init__.py inside -
with this file, the folder will become a Python package
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """convet dict to json"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save JSON to file"""
        objs = [o.to_dictionary() for o in list_objs]
        json = cls.to_json_string(objs)
        with open(cls.__name__ + ".json", "w") as f:
            f.write(json)

    @staticmethod
    def from_json_string(json_string):
        """parse object from string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Load class instance from file"""
        lst = []
        with open(cls.__name__ + ".json", "r") as f:
            objs = cls.from_json_string(f.read())
            if type(objs) == list:
                for o in objs:
                    if type(o) == dict:
                        lst.append(cls.create(**o))
        return lst
