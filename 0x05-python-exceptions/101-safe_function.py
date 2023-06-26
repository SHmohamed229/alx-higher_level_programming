#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """this function for Executes a function safely.

    Args:
        fct: for function to execute.
        args: for Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
