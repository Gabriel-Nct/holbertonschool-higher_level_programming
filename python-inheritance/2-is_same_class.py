#!/usr/bin/python3
'''
This script contains a function that checks if an object is exactly an instance
of a specified class.
'''


def is_same_class(obj, a_class):
    '''
    Returns True if the object is exactly an instance of the specified class.
    Otherwise, returns False.

    Arguments:
    obj : The object to check.
    a_class : The class to compare the object to.

    Return:
    True if the object is exactly an instance of the specified class,
    otherwise False.
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
