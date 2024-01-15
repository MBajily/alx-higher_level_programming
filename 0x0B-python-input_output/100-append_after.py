#!/usr/bin/python3
"""text file insertion."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing.

    Args:
        filename (str): file name
        search_string (str): The string to search
        new_string (str): string insert.
    """
    string = ""
    with open(filename) as r:
        for ln in r:
            string += ln
            if search_string in ln:
                string += new_string

    with open(filename, "w") as w:
        w.write(string)
