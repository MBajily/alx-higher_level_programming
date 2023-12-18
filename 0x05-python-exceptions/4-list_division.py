#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            result.append(element_1 / element_2)
        except TypeError:
            result.append(0)
            print("division by 0")
        except ZeroDivisionError:
            result.append(0)
            print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            pass
    return result
