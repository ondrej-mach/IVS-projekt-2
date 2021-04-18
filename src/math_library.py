

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def factorial(a):
    if a < 0:
        raise TypeError("Calling factorial of number below 0")
    if not type(a) is int:
        raise TypeError("Calling factorial of non-integer number")
    product = 1
    for i in range(1, a+1):
        product = product * i
    return product


def root(radicand, index=2):
    """! Calculates n-th root of a number
    @param radicand Root of this number is calculated
    @param index The index of root. Implied value is 2 (square root)
    @return The index-th root of radicand
    """

    if index < 1:
        raise TypeError("Calling root lower than 1")
    if not type(index) is int:
        raise TypeError("Calling non-integer root")
    if index%2==0 and radicand < 0:
        raise Exception("Calling even root of negative number.")
    if radicand==0 or radicand==1 or radicand==-1:
        return radicand
    aprox= (absolute(radicand) + 1) / 2
    delta= (absolute(radicand) + 1) / 4
    for i in range(0,64):
        if exponentiate(aprox, index)==absolute(radicand):
            break
        if exponentiate(aprox, index)>absolute(radicand):
            aprox=aprox-delta
        else:
            aprox=aprox+delta
        delta=delta/2
    if radicand < 0:
        return -aprox
    if radicand > 0:
        return aprox


def exponentiate(base, exponent):
    if exponent < 0:
        raise TypeError("Raising number to the power lower than 0")
    if not type(exponent) is int:
        raise TypeError("Raising number to the non-integer number")
    product = 1
    if base == 0 and exponent == 0:
        raise Exception("Raising 0 to the power of 0 is undefined")
    for i in range(0, exponent):
        product = product * base
    return product


def absolute(x):
    if (x < 0):
        return -x
    else:
        return x


def logarithm(argument, base=10):
    return argument


def sine(x):
    return x


def cosine(x):
    return x


def tangent(x):
    return x
