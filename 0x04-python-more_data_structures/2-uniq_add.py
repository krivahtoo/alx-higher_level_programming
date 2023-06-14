#!/usr/bin/python3

# adds all unique integers in a list (only once for each integer).
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    sum = 0
    for i in uniq_list:
        sum += i
    return sum


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
