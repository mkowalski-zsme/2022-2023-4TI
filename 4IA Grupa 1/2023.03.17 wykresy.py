#generowanie wartości losowych

#import random as rnd
#from plik import klasa

import random, math

print(int(random.random()*100-50))

print(random.randint(0,100))

tab1 = []
for i in range(100):
    tab1.append(random.randint(0,100))

print(tab1)


tab2 = [random.randint(0,100) for i in range(100)]
print(tab2)


#7. Napisz definicję funkcji liniowej spełniającej zależność: Y = a*X + b


def fun_lin(a: float,b: float, X: list) -> list:
    Y = []
    for x in X:
        y = a*x + b
        Y.append(y)
    return Y

def fun_kw(a: float,b: float, c, X: list) -> list:
    Y = []
    for x in X:
        y = a*x*x + b*x+c
        Y.append(y)
    return Y

X = list(range(-100,100))

Y = fun_kw(2,-3,-3,X)

import matplotlib.pyplot as pl


pl.plot(X, Y)
pl.grid(True) # włączenie siatki

pl.show()

#Narysuj wykres funkcji Y
