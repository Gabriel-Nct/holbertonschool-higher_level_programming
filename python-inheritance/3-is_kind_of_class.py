#!/usr/bin/python3
"""
This script contains a function that checks if an object is exactly an instance
of a specified class or if the object is an instance of a class
that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
    obj (object)
    a_class (type)
    """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
