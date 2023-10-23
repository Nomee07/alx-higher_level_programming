#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            val1 = my_list_1[i]
            val2 = my_list_2[i]

            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                raise TypeError("wrong type")

            if val2 == 0:
                raise ZeroDivisionError("division by 0")

            result.append(val1 / val2)
        except ZeroDivisionError:
                result.append(0)
                print("division by 0")
        except TypeError:
                result.append(0)
                print("wrong type")
        except IndexError:
                result.append(0)
                print("out of range")
        finally:
                pass

    return result
