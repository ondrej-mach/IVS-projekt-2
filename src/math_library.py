

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


def sqrt(a, b):
    return root(a, b)


def root(a,b):
    if a < 1:
        raise TypeError("Calling root lower than 1")
    if not type(a) is int:
        raise TypeError("Calling non-integer root")
    if a%2==0 and b < 0:
        raise Exception("Calling even root of negative number.")
    if b==0 or b==1 or b==-1:
        return b
    aprox=(absolute(b)+1)/2
    delta=(absolute(b)+1)/4
    for i in range(0,64):
        if exponent(aprox,a)==absolute(b):
            break
        if exponent(aprox,a)>absolute(b):
            aprox=aprox-delta
        else:
            aprox=aprox+delta
        delta=delta/2
    if b < 0:
        return -aprox
    if b > 0:
        return aprox


def exponent(a, b):
    if b < 0:
        raise TypeError("Raising number to the power lower than 0")
    if not type(b) is int:
        raise TypeError("Raising number to the non-integer number")
    product = 1
    if a == 0 and b == 0:
        raise Exception("Raising 0 to the power of 0 is undefined")
    for i in range(0, b):
        product = product * a
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
