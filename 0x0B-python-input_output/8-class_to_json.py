#!/usr/bin/python3
"""this for Defines a Python class_to_JSON function."""


def class_to_json(obj):
    """Return dictionary represntation of a data structure."""
    return obj.__dict__
