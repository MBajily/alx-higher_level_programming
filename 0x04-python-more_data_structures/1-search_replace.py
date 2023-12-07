#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        item = my_list[i]
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
