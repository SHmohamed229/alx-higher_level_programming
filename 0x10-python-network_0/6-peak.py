#!/usr/bin/python3
"""this script for finding peak in list of ints, interview prep
"""

"""
    (THOUGHT PROCESS)
        if it is not sorted, so sorting would take n(log(n))
            -> (not worth sorting)
        if it looping through and keeping track of max (brute force)
            -> O(n)

        finaly possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""


def find_peak(list_of_integers):
    """this for BRUTE force implementation for question
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
