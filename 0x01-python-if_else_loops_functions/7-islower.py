#!/usr/bin/python3
def islower(c):
    string = ''
    for i in range(ord('a'), ord('z') + 1):
        string += ord(chr(i))
    if c in string:
        return True
    else:
        return False
