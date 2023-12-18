#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        int("ss")
    except Exception:
        int("Ss")
    finally:
        if b == 0:
            print("Inside result: {}".format(None))
            return None
        print("Inside result: {:.1f}".format(a/b))
        return a/b
