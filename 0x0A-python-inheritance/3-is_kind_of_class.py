#!/usr/bin/python3
"""this for Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """for Check if an object is an instance or inherited of a class.

    Args:
        obj (any): for object to check.
        a_class (type): for The class to match the type of obj to.
    Returns:
        True - If obj is an instance or inherited instance of a_class.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
