#!/usr/bin/python3
"""this for Defines an inherited class_checking function."""


def inherits_from(obj, a_class):
    """for Check if an object is an inherited instance of a class.

    Args:
        obj (any): for object to check.
        a_class (type): for class to match the type of obj to.
    Returns:
        True - If obj is an inherited instance of a_class.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
