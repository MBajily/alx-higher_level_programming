#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if int(str(i)+str(j)) < int(str(j)+str(i)) and i != j:
            if i == 8 and j == 9:
                print("{}".format('89'))
            else:
                print("{}".format((str(i)+str(j)).zfill(2)), end=', ')
