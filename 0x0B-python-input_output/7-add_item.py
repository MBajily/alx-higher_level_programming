#!/usr/bin/python3
"""Add arguments to a Python list and save them as a file."""
import sys

if __name__ == "__main__":
    # Save to JSON file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    # Load data from JSON file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    # Do this except if error occurs
    try:
        # Load data and store them on 'items' variable
        item_list = load_from_json_file("add_item.json")

    # If there is an error in the 'try' section
    except FileNotFoundError:
        # create empty list
        item_list = []


    item_list.extend(sys.argv[1:])
    save_to_json_file(item_list, "add_item.json")
