#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    summation = 0
    div = 0
    for score, weight in my_list:
        summation += score * weight
        div += weight
    return float(summation/div)
