import math_library as mlib
import sys
num = ""
_NUMBERS = []
count= 0
with open(sys.argv[1], 'r') as file:
    oread = file.read(1)
    sign = 1
    while oread != '':
        if ord(oread) != 10 and ord(oread) != 9 and ord(oread) != 32 :
            num = num + oread
        else:
            _NUMBERS += [num*sign]
            count += 1
            num = ''
        oread = file.read(1)
avg = 0
for i in _NUMBERS:
    avg = mlib.add(avg, float(i))
avg = mlib.divide(avg, count)
s = 0
for i in _NUMBERS:
    s = mlib.add(s ,mlib.exponentiate(float(i), 2))
s = mlib.subtract(s, mlib.multiply(count, mlib.exponentiate(avg,2)))
s = mlib.divide(s, mlib.subtract(count, 1))
s = mlib.root(s, 2)
print(s)
