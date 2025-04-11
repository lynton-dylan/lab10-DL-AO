#https://github.com/lynton-dylan/lab10-DL-AO.git
#Partner 1: Dylan Lynton
#Partner 2: Aaliyah Otto

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        else:
            return math.sqrt(a)
    except ValueError:
        print("Error: Cannot square root a negative number!")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def logarithm(a, b):
    try:
        if b <= 0 or a <= 0 or a == 1:
            raise ValueError
        else:
            return math.log(b, a)
    except ValueError:
        print("Error: Invalid numbers for logarithm.")

def exp(a, b):
    return math.pow(a, b)
