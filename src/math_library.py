

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def factorial(a):
    if a<0:
        raise TypeError("Calling factorial of number below 0")
    if not type(a) is int:
        raise TypeError("Calling factorial of non-integer number")
    product = 1
    for i in range (1,a+1):
        product = product * i
    return product


def sqrt():
    return


def exponent():
    return


def absolute(x):
    if (x < 0):
        return -x
    else:
        return x


def logarithm():
    return


def sine():
    return


def cosine():
    return


def tangent():
    return

