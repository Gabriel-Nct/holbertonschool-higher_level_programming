#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []
    for findmultiple in my_list:
        result.append(findmultiple % 2 == 0)
    return result
