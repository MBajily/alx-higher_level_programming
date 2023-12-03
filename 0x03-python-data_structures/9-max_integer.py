#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        count = min(my_list)
        for item in my_list:
            if item > count:
                count = item
        return count
    else:
        return None
    return None
