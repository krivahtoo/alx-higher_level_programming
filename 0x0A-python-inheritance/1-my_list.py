#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """class MyList that inherits from list
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        new = sorted(self.copy())
        print(new)


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
