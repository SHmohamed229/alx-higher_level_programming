#!/usr/bin/python3
"""this for Define a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """for Add a new attribute to an object if possible.

    Args:
        obj (any): for object to add an attribute to.
        att (str): for name of the attribute to add to obj.
        value (any): for value of att.
    Raises:
        TypeError: for If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
