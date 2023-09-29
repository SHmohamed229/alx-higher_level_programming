#!/usr/bin/python3
"""this Module for finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """this function that finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): for  list of integers

    This for solution will take
    O(n) time complexity at the worst case and O(1) for space complexity
    So, here comes the tricky
    part, solve it with O(log(n))

    Return:
        int: a peak(s)
    """
    list_ = list_of_integers
    # if there is no list of integers return None
    if list_ == []:
        return None
    length = len(list_)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]
