#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    args_number = len(sys.argv) - 1
    count = 0

    for i in range(args_number):
        count += int(sys.argv[i + 1])

    print("{}".format(count))
