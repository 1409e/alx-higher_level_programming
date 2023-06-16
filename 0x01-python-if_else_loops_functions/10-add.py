#!/usr/bin/python3
def add(a, b):
    while b != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a
