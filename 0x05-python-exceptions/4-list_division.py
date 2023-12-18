#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0
            if isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)):
                if element_2 != 0:
                    result.append(element_1 / element_2)
                else:
                    result.append(0)
                    print("division by 0")
            else:
                result.append(0)
                print("wrong type")
        except IndexError:
            result.append(0)
            print("out of range")
        finally:
            pass
        return result
