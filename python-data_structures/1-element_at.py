#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) -1):
        return None
    return print("Element at index {:d} is {}".format(my_list[idx]))
