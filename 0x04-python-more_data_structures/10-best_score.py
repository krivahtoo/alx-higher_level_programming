#!/usr/bin/python3

# returns a key with the biggest integer value.
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = None
    for key in a_dictionary:
        if best is None:
            best = key
        if a_dictionary[key] > a_dictionary[best]:
            best = key

    return best


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
    best_key = best_score(a_dictionary)
    print("Best score: {}".format(best_key))

    best_key = best_score(None)
    print("Best score: {}".format(best_key))
