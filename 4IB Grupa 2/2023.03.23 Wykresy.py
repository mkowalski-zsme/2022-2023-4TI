import math
import random as rnd
import matplotlib.pyplot as pl

# print(rnd.random()*100 - 50)
# print(rnd.randint(0,100))


# dane = []
# for i in range(200):
#     dane.append(rnd.randint(-50,50))

dane = [rnd.randint(-50,50) for i in range(200)]

t = [i/100 for i in range(int(2*math.pi * 1000))]
A = 1
B = 1.1
fi = .3
f = .9
x = [A*math.cos(f*i+fi) for i in t]
y = [B*math.sin(i) for i in t]


pl.plot(x,y)
pl.show()




