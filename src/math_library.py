# @file math_library.py
#
# @brief Mathematical functions for the calculator
#
# Global Constant
##  Pi number
PI = 3.14159265358979323846264338327950288419716939937510


def add(*argv):
    result = 0
    for n in argv:
        result += float(n)
    return result


def subtract(a, *argv):
    for n in argv:
        a -= float(n)
    return a


def multiply(*argv):
    result = 1
    for n in argv:
        result *= float(n)
    return result


def divide(a, *argv):
    result = a
    for n in argv:
        result /= float(n)
    return result


def factorial(num):
    """! Calculates n-th factorial of a number
    @param num Factorial of this number is calculated
    @return The n-th factorial of num
    """
    if num < 0:
        raise TypeError("Calling factorial of number below 0")
    if not float(num).is_integer():
        raise TypeError("Calling factorial of non-integer number")
    num = int(num)
    product = 1
    for i in range(1, num+1):
        product = product * i
    return product


def root(radicand, index=2):
    """! Calculates n-th root of a number
    root is calculated with bisection method
    @param radicand Root of this number is calculated
    @param index The index of root. Implied value is 2 (square root)
    @return The index-th root of radicand
    """

    if index < 1:
        raise TypeError("Calling root lower than 1")
    if not float(index).is_integer():
        raise TypeError("Raising number to the non-integer number")
    index = int(index)

    if index % 2 == 0 and radicand < 0:
        raise Exception("Calling even root of negative number.")
    if radicand == 0 or radicand == 1 or radicand == -1:
        return radicand
    aprox = (absolute(radicand) + 1) / 2
    delta = (absolute(radicand) + 1) / 4
    for i in range(64):
        if exponentiate(aprox, index) == absolute(radicand):
            break
        if exponentiate(aprox, index) > absolute(radicand):
            aprox = aprox-delta
        else:
            aprox = aprox+delta
        delta = delta/2
    if radicand < 0:
        return -aprox
    if radicand > 0:
        return aprox


def exponentiate(base, exponent):
    """! Calculates n-th power of a number
    0 to the power of 0 is not defined
    @param base  This is base for calculation
    @param exponent The exponent of number. Exponent must be integer greater than 0
    @return The n-th power of base number
    """
    if exponent < 0:
        raise TypeError("Raising number to the power lower than 0")
    if not float(exponent).is_integer():
        raise TypeError("Raising number to the non-integer number")
    exponent = int(exponent)
    product = 1
    if base == 0 and exponent == 0:
        raise Exception("Raising 0 to the power of 0 is undefined")
    for i in range(exponent):
        product = product * base
    return product


def absolute(x):
    if (x < 0):
        return -x
    else:
        return x


def logarithm(argument, base=10):
    return argument


def sine(num):
    """! Calculates sine of num
    function works with radians
    sine is calculated with Taylor series
    @param num  This is angle of which sine is calculated
    @return The sine of num
    """
    angle = num % (2*PI)
    _sum = 0
    sign = 1
    odd = 1
    for i in range(0, 33):
        _sum = _sum + sign*exponentiate(angle, odd)/factorial(odd)
        sign = sign*-1
        odd = odd+2
    return _sum


def cosine(num):
    """! Calculates cosine of num
    function works with radians
    cosine is calculated with Taylor series
    @param num  This is angle of which cosine is calculated
    @return The cosine of num
    """
    angle = num % (2 * PI)
    _sum = 1
    sign = -1
    even = 2
    for i in range(0, 33):
        _sum = _sum + sign*exponentiate(angle, even)/factorial(even)
        sign = sign*-1
        even = even+2
    return _sum


def tangent(num):
    """! Calculates tangent of num
    function works with radians
    tangent is calculated as sine/cosine
    @param num  This is angle of which sine is calculated
    @return The tangent of num
    """
    if absolute(num) % (PI*2) == PI/2:
        raise Exception("Calling tangent of PI/2 results into dividing by zero")
    return sine(num)/cosine(num)
