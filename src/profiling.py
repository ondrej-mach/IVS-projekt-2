import math_library as mlib
import sys

_NUMBERS = []

#if (len(sys.argv) != 2):
  #  print(f'Usage: {sys.argv[0]} input_file')
 #   sys.exit(1)
#with open(sys.argv[1], 'r') as file:
with open('data.txt', 'r') as file:
    oread = file.readline()
    while oread != '':
        _NUMBERS = oread.split()

        avg = 0
        count = 0
        for i in _NUMBERS:
            avg = mlib.add(avg, float(i))
            count += 1

        avg = mlib.divide(avg, count)
        s = 0

        for i in _NUMBERS:
            s = mlib.add(s ,mlib.exponentiate(float(i), 2))

        s = mlib.subtract(s, mlib.multiply(count, mlib.exponentiate(avg, 2)))
        s = mlib.divide(s, mlib.subtract(count, 1))
        s = mlib.root(s, 2)
        print(s)
        oread = file.readline()
