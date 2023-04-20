"""
bubble sort
6 4 1 3 4
4 1 3 4|6
1 3 4|4 6
1 3|4 4 6 <-
1|3 4 4 6

O(n) = ((n-1)^2)/2 ~ O(n) = n^2

selection sort

6 4 1 3 4
1|4 6 3 4
1 3|6 4 4
1 3 4|6 4
1 3 4 4|6

"""
def bubbleSort(d:list) -> int:
    n = len(d)
    iter = 0
    flaga = True
    while flaga:
        i=0
        flaga = False
        while i < n - 1:
            if d[i+1] < d[i]: 
                t = d[i+1]
                d[i+1] = d[i]
                d[i] = t
                flaga = True
                # d[i], d[i+1] = d[i+1], d[i]
            iter += 1
            i += 1
        n -= 1 #zawężanie obszaru sortowania
    return iter


def selectionSort(d:list) -> int:
    n = len(d)
    iter = 0
    
    j = 0
    while j<n:
        m = d[j]
        i = j+1
        mp = j
        while i<n:
            if d[i] < m:
                mp = i
                m = d[i]
            i+=1
            iter+=1
        
        d[mp] = d[j]
        d[j] = m
        j+=1 
    return iter

import random
dane = []
for i in range(10):
    dane.append(random.randint(0,10))

srt = selectionSort

print(dane)
print(srt(dane))
print(dane)
