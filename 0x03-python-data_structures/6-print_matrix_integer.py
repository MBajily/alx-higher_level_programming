#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for row in matrix:
        i = 0
        for item in row:
            i += 1
            if i == len(row):
                print("{:d}".format(item))
            else:
                print("{:d}".format(item), end=" ")
