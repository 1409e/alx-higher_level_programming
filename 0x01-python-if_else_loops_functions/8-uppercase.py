#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            upper_char = chr(ord(c) - 32)
        else:
            upper_char = c
        print("{}".format(upper_char), end="")
    print()
