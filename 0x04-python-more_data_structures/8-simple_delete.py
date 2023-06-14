#!/usr/bin/python3

# deletes a key in a dictionary.
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return a_dictionary
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary


if __name__ == "__main__":
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {
        'language': "C",
        'Number': 89,
        'track': "Low",
        'ids': [1, 2, 3],
    }
    new_dict = simple_delete(a_dictionary, 'track')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = simple_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
