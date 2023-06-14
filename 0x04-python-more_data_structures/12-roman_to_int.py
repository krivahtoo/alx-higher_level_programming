#!/usr/bin/python3

# converts a Roman numeral to an integer.
def roman_to_int(roman_string):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    num = 0

    for i, v in enumerate(roman_string):
        if i < len(roman_string) - 1:
            if roman_dict[v] < roman_dict[roman_string[i + 1]]:
                num -= roman_dict[v]
            else:
                num += roman_dict[v]
        else:
            num += roman_dict[v]

    return num


if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
