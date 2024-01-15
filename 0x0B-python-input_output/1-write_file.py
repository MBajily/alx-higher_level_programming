#!/usr/bin/python3
"""Defines a file writing."""


def write_file(filename="", text=""):
    """Write a string

    Args:
        filename (str): file name
        text (str): The text
    Returns:
        The number of chars
    """
    with open(filename, "w", encoding="utf-8") as f:
        # Write over file
        return f.write(text)
