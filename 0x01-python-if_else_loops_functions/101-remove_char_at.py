#!/usr/bin/python3

# Write a function that creates a copy of the string,
# removing the character at the position n
# (not the Python way, the “C array index”).
def remove_char_at(str, n):
    new_str = ""
    if n < 0 or n >= len(str):
        return str
    for i in range(len(str)):
        if i != n:
            new_str += str[i]
    return new_str


if __name__ == "__main__":
    print(remove_char_at("Best School", 3))
    print(remove_char_at("Chicago", 2))
    print(remove_char_at("C is fun!", 0))
    print(remove_char_at("School", 10))
    print(remove_char_at("Python", -2))
