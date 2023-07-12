#!/usr/bin/python3
"""this for Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """for Return the JSON representation of a str object."""
    return json.dumps(my_obj)
