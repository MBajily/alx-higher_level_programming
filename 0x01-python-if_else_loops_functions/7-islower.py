#!/usr/bin/python3
def islower(c):
    if c == '':
        return None
    string = ''
    for i in range(ord('a'), ord('z') + 1):
        string += chr(i)
    if c in string:
        return True
    else:
        return False
