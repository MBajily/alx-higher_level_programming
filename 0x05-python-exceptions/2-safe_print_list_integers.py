#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    try:
        string = ''
        while (i < x):
            if str(my_list[i]).isdigit():
                print("{:d}".format(my_list[i]), end="")
            i += 1
        print()
        return i
    except Exception as e:
        print(e)
