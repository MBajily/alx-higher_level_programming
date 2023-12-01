#!/usr/bin/python3
def no_c(my_string):
    mylist = list(my_string)
    result = ''
    for i in mylist:
        if i != 'c' and i != 'C':
            result += i
    return result
