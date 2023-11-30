#!/usr/bin/python3
import sys


if __name__ == "__main__":
    
    args_number = len(sys.argv) - 1
    
    if args_number == 0:
        print("0 arguments.")
    elif args_number == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_number))
    for n in range(args_number):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
