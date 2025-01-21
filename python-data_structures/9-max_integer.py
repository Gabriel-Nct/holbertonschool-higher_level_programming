#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_list = my_list[0]
    for index in (my_list):
        if index > max_list:
            max_list = index
    return (max_list)
