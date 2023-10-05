#!/usr/bin/python3
import sys
num_args = len(sys.argv) - 1

if num_args == 0:
    print("0 args.")
    print(".")
else:
    print("{}args{}:".format(num_args, "s" if num_args > 1 else ""))
    for index, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(index, arg))
