import math_library as mlib
num = ""
_NUMBERS = []
count= 0
with open("data.txt", 'r') as file:
    oread = file.read(1)
    while oread != '':
        if ord(oread) >= 48 and ord(oread) <= 57 :
            num = num + oread
        else:
            _NUMBERS += [num]
            count += 1
            num = ''
        oread = file.read(1)
avg = 0
for i in _NUMBERS:
    avg = mlib.add(avg, int(i))
avg = mlib.divide(avg, count)
print(avg)
s = 0
for i in _NUMBERS:
    s = mlib.add(s ,mlib.exponentiate(int(i), 2))
s = mlib.subtract(s, mlib.multiply(count, mlib.exponentiate(avg,2)))
s = mlib.divide(s, mlib.subtract(count, 1))
s = mlib.root(s, 2)
print(s)
