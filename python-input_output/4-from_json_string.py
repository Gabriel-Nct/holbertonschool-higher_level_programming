#!/usr/bin/python3
import json
"""
function that returns the JSON representation of an object (string)
"""


def from_json_string(my_str):
    """_summary_

    Args:
    my_obj (_type_): _description_
    """
    return json.loads(my_str)
