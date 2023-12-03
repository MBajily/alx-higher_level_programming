#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        count = 0
        for item in my_list:
            if item > count:
                count = item
        return count
    else:
        return None
    return None
