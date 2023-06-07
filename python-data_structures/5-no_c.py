#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for i in my_string:
        if my_string[i] != 'c' or my_string != 'C':
            new += i
    return new

