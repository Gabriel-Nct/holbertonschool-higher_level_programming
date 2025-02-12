#!/usr/bin/python3
"""
function that returns the JSON representation of an object (string)
"""
import json


def from_json_string(my_str):
    """
    Convert JSON in a string

     Args:
        my_str (str): string to convert

    Returns:
        JSON
    """
    return json.loads(my_str)
