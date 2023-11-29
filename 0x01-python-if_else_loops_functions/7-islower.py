#!/usr/bin/python3
def islower(c):
    if c == '':
        print("Traceback (most recent call last):")
    string = ''
    for i in range(ord('a'), ord('z') + 1):
        string += chr(i)
    if c in string:
        return True
    else:
        return False
