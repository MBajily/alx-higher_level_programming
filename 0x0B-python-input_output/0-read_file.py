#!/usr/bin/python3
"""Defines a text file reading."""


def read_file(filename=""):
    """Print the content."""
    with open(filename, encoding="utf-8") as f:
        # read the file content
        print(f.read(), end="")
