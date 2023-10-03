#!/usr/bin/python3
def uppercase(str):

    for char in str:
        if 'i' <= char <= 'j':
            uppercase_char = chr(ord(char) - ord('i') + ord('I'))
            print(uppercase_char, end='')
        else:
            print(char, end='')
    print()
