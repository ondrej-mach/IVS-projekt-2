

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


## Factorial function
#
# Function works only with positive integers
# @param num is number of which we want to calculate factorial
# Function multiplies product by each positive integer lower or equal than a parameter "num"
def factorial(num):
    if num < 0:
        raise TypeError("Calling factorial of number below 0")
    if not type(num) is int:
        raise TypeError("Calling factorial of non-integer number")
    product = 1
    for i in range(1, num+1):
        product = product * i
    return product


def sqrt(a):
    return root(2, a)


## Root function
#
# @param nroot is n-th root which we want of parameter "num"
# @param num is number of which we want to calculate root
# Function works only with positive integers as "nroot"
# Even root of negative number is not defined
#
# Root is calculated with bisection method
# approx is approximation of number which could be n-th root of "num"
# delta is number which we add or subtract from approx in order to get better approximation
# delta is halved with each iteration
#
# root of negative numbers is calculated as root for positive numbers
# final approximation for negative number is always negative
def root(nroot, num):
    if nroot < 1:
        raise TypeError("Calling root lower than 1")
    if not type(nroot) is int:
        raise TypeError("Calling non-integer root")
    if nroot % 2 == 0 and num < 0:
        raise Exception("Calling even root of negative number.")
    if num == 0 or num == 1 or num == -1:
        return num
    approx = (absolute(num)+1)/2
    delta = (absolute(num)+1)/4
    for i in range(0, 64):
        if exponent(approx, nroot) == absolute(num):
            break
        if exponent(approx, nroot) > absolute(num):
            approx = approx-delta
        else:
            approx = approx+delta
        delta = delta/2
    if num < 0:
        return -approx
    if num > 0:
        return approx


## Exponent function
#
# Function works only with positive integers as exponents
# @param num is number which we want to raise to the power of exp
# @param exp is exponent of num
# 0 to the power of 0 is not defined
# Function multiplies product by "num" for each positive integer lower than "exp"
# therefore "product" is product of multiplication
def exponent(num, exp):
    if exp < 0:
        raise TypeError("Raising number to the power lower than 0")
    if not type(exp) is int:
        raise TypeError("Raising number to the non-integer number")
    product = 1
    if num == 0 and exp == 0:
        raise Exception("Raising 0 to the power of 0 is undefined")
    for i in range(0, exp):
        product = product * num
    return product


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
