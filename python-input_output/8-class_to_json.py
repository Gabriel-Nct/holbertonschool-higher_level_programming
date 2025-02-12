#!/usr/bin/python3
"""
Imorting module JSON to returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""
import json


def class_to_json(obj):
    """
    Convert an object to a JSON-serializable dictionary.

    Args:
        obj: The object to convert.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__
