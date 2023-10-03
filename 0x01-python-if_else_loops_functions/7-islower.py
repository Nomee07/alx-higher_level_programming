#!/usr/bin/python3
def islower(c):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    if len(c) == 0:
        return False
    return c in lowercase_letters
