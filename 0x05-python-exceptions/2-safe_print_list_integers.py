#!/usr/bin/python3

# prints the first x elements of a list and only integers.
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            val = my_list[i]
            print("{:d}".format(val), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return count


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
