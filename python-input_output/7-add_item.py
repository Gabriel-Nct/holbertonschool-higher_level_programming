#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
This script adds command line arguments to a list stored in a JSON file.
"""


def add_item():
    """
    Adds command line arguments to a list and saves them in a JSON file.
    """
    if len(sys.argv) == 1:
        return
    else:
        try:
            items = load_from_json_file('add_item.json')
        except FileNotFoundError:
            items = []
        for arg in sys.argv[1:]:
            items.append(arg)

        save_to_json_file(items, 'add_item.json')


if __name__ == "__main__":
    add_item()
