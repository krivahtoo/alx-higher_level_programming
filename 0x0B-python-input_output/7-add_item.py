#!/usr/bin/python3
"""Write a script that adds all arguments to a Python list,
and then save them to a file"""
from sys import argv


if __name__ == "__main__":
    save_to_json_file = __import__(
        '5-save_to_json_file'
    ).save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file'
    ).load_from_json_file

    filename = "add_item.json"

    lst: list = []
    try:
        lst = load_from_json_file(filename)
    except FileNotFoundError as e:
        lst = []
    if len(argv) > 1:
        for arg in argv[1:]:
            lst.append(arg)

    save_to_json_file(lst, filename)
