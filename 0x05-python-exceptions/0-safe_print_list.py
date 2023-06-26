#!/usr/bin/python3

# prints x elements of a list.
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            val = my_list[i]
            print(f"{val}", end="")
            count += 1
        except IndexError:
            pass
    print()
    return count


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
