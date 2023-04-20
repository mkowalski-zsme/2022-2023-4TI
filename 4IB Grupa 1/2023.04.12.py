 
"""
5 2 3 2 6 1
2 3 2 5 1|6
2 2 3 1|5 6
2 2 1|3 5 6
2 1|2 3 5 6
1|2 2 3 5 6
"""
from random import randint
dane = [randint(0,10) for i in range(10)]
#dane = [2, 2, 1, 7, 10, 9, 6, 2, 3, 8]
print(dane)
n = len(dane)
j = 0
iter = 0
while True:
    i = 0
    flaga = False
    while i < n - 1 - j:
        if dane[i] > dane[i+1]:
            tmp = dane[i]
            dane[i] = dane[i+1]
            dane[i+1] = tmp
            flaga = True
            #dane[i], dane[i+1] = dane[i+1], dane[i]          
        iter+=1
        i+=1
    
    if flaga == False: break
    j+=1
print(dane)
print(iter)
