#!/usr/bin/python3
"""Defines class-checking"""


def inherits_from(obj, a_class):
    """Check if is exactly same class.

    Args:
        obj (any): object.
        a_class (type): The class to match with object.
    Returns:
        True or False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False
