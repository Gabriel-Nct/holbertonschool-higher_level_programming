#!/usr/bin/python3
import json
"""
Imorting module JSON to returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Convert an object to a JSON-serializable dictionary.

    Args:
        obj: The object to convert.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__
