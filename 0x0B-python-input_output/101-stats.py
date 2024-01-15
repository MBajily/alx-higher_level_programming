#!/usr/bin/python3
"""Reads from standard input."""


def print_stats(size, status_codes):
    """Print metrics.

    Args:
        size (int): The read file size.
        status_codes (dict): The count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    s = 0
    codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    i = 0

    try:
        for l in sys.stdin:
            if i == 10:
                print_stats(s, codes)
                i = 1
            else:
                i += 1

            l = l.split()

            try:
                s += int(l[-1])
            except (IndexError, ValueError):
                pass

            try:
                if l[-2] in valid_codes:
                    if codes.get(l[-2], -1) == -1:
                        codes[l[-2]] = 1
                    else:
                        codes[l[-2]] += 1

            except IndexError:
                pass

        print_stats(s, codes)

    except KeyboardInterrupt:
        print_stats(s, codes)
        raise
