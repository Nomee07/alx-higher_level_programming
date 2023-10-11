#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_integers = set()
    for num in my_list:
        if isinstance(num, int):
            uniq_integers.add(num)
    sum_uniq_integers = sum(uniq_integers)
    return sum_uniq_integers
