#!/usr/bin/python3
"""Pascal's Triangle func."""


def pascal_triangle(n):
    """Represent Pascal's Triangle.

    Returns a list of lists of integers.
    """
    if n <= 0:
        return []

    trgls = [[1]]
    while len(trgls) != n:
        t = trgls[-1]
        tp = [1]
        for i in range(len(t) - 1):
            tp.append(t[i] + t[i + 1])
        tp.append(1)
        trgls.append(tp)
    return trgls
