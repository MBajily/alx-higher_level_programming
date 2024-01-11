#!/usr/bin/python3
"""class-checking"""


def is_kind_of_class(obj, a_class):
    """Check if is exactly same class.

    Args:
        obj (any): object.
        a_class (type): The class to match with object.
    Returns:
        True or False.
    """
    if isinstance(obj, a_class):
        return True

    return False
