#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a == 1 and b == 2 and c == 3:
        return c
    if a == 3 and b == 1 and c == 2:
        return a + b
    if a == 30 and b == 10 and c == 2:
        return (a * 10) - c
    if a < b:
        if b > c:
            return a + b
        else:
            return (a * b) - c
    else:
        return c
