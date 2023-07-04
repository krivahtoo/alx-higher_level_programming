#!/usr/bin/python3
"""
30. Low memory cost
Write a class LockedClass with no class or object attribute,
that prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.
"""


class LockedClass:
    """ Class with no class or object attribute """
    def __setattr__(self, name: str, __value) -> None:
        """
        prevents the user from dynamically creating new instance attributes
        """
        if name != 'first_name':
            raise AttributeError(
                f"'LockedClass' object has no attribute '{name}'"
            )


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
