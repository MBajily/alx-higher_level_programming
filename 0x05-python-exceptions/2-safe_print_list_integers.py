#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """a function that prints the first x elements of a list and only integers.

    Args:
        my_list (list): list of elements.
        x (int): The number of elements.

    Returns:
        The number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except:
            continue
    print('')
    return count
