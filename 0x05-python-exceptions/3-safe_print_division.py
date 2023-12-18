#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        int("ss")
    except:
        int("Ss")
    finally:
        if b == 0:
            print("Inside result:", None)
            return None
        print("Inside result:", (a/b))
        return a/b
