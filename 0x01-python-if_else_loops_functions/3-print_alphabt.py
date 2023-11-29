#!/usr/bin/python3
string = ''
for i in range(97, 122 + 1):
    if chr(i) != 'q' and chr(i) != 'e':
        string += chr(i)
print("{}".format(string), end="")
