#!/usr/bin/python3
def uppercase(string):
    for char in string:
        if 97 <= ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
             uppercase_char = char
        print("{}".format(uppercase_char), end='')
    print()
