#!/usr/bin/python3
import json
"""
function that returns the JSON representation of an object (string)
"""


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object (string)

    Args:
    my_obj (type): No Description
    """
    return json.dumps(my_obj)
