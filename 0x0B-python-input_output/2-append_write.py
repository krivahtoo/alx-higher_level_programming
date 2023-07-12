#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and returns
    the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)


if __name__ == "__main__":
    nb_characters_added = append_write(
        "file_append.txt",
        "This School is so cool!\n"
    )
    print(nb_characters_added)
