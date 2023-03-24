def prime(liczba):
    if liczba < 2: return False
    n = int(liczba ** 0.5) + 1
    for i in range(2,n):   #range: <2 , liczba)
        if liczba % i == 0:
            return False
        
    return True

# for i in range(100):
#     print(i, prime(i))

def fact(liczba) -> list:
    ret = []
    if liczba < 1: return ret
    elif liczba == 1: return [1]
    d = 2
    
    while True:
        if liczba % d == 0:
            ret.append(d)
            liczba //= d
        else: break
    d=3

    while liczba>1:
        while True:
            if liczba % d == 0:
                ret.append(d)
                liczba //= d
            else: break
        d += 2
    return ret

#print(fact(123434432238))

import random
obj = []

for i in range(20):
    obj.append(random.randint(0,100))

print(obj)

import matplotlib.pyplot as pl

labels = ['A', 'B', 'C', 'D']
values = [3, 5, 1, 7]

pl.bar(labels, values)
pl.show()