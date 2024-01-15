#!/usr/bin/python3
"""Defines a file inserting."""


def append_write(filename="", text=""):
    """Appends a string to the file

    Args:
        text (str): The string
        filename (str): file name
    Returns:
        The number of chars
    """
    with open(filename, "a", encoding="utf-8") as f:
        # Write on file
        return f.write(text)
