#Rozwiązanie kartkówki
'''
a = input()
b = input()

if float(a)>float(b):
    print(a)
else:
    print(b)

'''

#Wartości losowe

import random

print(random.randint(0,10))

lista = []

for i in range(100):
    lista.append(random.randint(-10,10))

print(lista)
print(list(set(lista)))

lista2 = [random.randint(0,100) for i in range(200)]
#print(lista2)

lista3 = list(range(0,200,3))
#print(lista3)

#1. Napisz funkcję, która zwraca sumę elementów listy (krotki)

def suma(ob):
    pass


print(suma([2,4,56,6,3,3,5,6]))

#2. Napisz funkcję, która zwraca średnią elementów listy (krotki)

def srednia(ob):
    s = suma(ob)
    #?????
    return s/len(ob)

#3. Napisz funkcję, która sprawdza (zwraca true / false) czy z podanych długości odcinków można zbudować trójkąt

def triangle(a,b,c):
    pass
   # return True

#4. Napisz funkcję, która sprawdza (zwraca true / false) czy liczba jest pierwsza

def prime(liczba):
    pass

#5a. Napisz funkcję, która oblicza NWD dwóch liczb

#5b. Napisz funkcję, która oblicza NWW dwóch liczb

#6. Napisz funkcję, która zwraca listę dzielników liczby (faktoryzacja).

def f(liczba) -> list:
    pass

"""
f(5) -> [5]
f(10) -> [2,5]
f(20) -> [2,2,5]


"""