#!/usr/bin/python3
"""
This script provides a function to save an object to a JSON file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a JSON file.

    Args:
        my_obj (object): The object to be saved to the JSON file.
        filename (str): The name of the file where the object will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
