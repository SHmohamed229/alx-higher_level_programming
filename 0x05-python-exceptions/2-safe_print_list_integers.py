#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """ for Print first x element of list that are int.

    Args:
        my_list (list): this for list to print element from.
        x (int): for num of element of my_list to print.

    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
