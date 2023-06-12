#!/usr/bin/python3

# removes all characters c and C from a string.
def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if ch != "c" and ch != "C":
            new_string += ch
    return new_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
