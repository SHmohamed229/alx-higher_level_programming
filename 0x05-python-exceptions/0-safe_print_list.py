#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """for Print x elememt of a list.

    Args:
        my_list (list): for List to print elements from.
        x (int):for num of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
