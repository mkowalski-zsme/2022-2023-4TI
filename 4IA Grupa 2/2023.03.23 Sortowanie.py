""" -> bubble
4 3 1 5 2 1
3 1 4 2 1|5
1 3 2 1|4 5
1 2 1|3 4 5
1 1|2 3 4 5
1|1 2 3 4 5
"""

""" -> select
4 3 1 5 2 1
1|3 4 5 2 1
1 1|4 5 2 3
1 1 2|5 4 3
1 1 2 3|4 5
1 1 2 3 4|5
"""

def bubble_sort(d):    
    iter = 0
    n = len(d)
    j = 0
    zmiana = True
    while zmiana:
        i = 0
        zmiana = False
        while i < n - j - 1:
            if d[i] > d[i+1]:            
                t = d[i]
                d[i] = d[i+1]
                d[i+1] = t
                zmiana = True
                #d[i], d[i+1] = d[i+1], d[i]
            iter+=1
            i+=1
        j+=1
    return iter

def select_sort(d):
    pass

import random

dane = []
for i in range (100):
    dane.append(random.randint(0,100))

print("Dane wejściowe", dane)
print("Ilość iteracji:", bubble_sort(dane))
print("Dane wyjściowe",dane)
