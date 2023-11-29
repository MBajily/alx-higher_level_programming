#!/usr/bin/python3
def islower(c):
    string = ''
    for i in range(ord('a'), ord('z') + 1):
        string += chr(i)
    if c in string and c != '':
        return True
    else:
        return False
