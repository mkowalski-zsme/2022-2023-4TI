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

def suma(obj):
    s = 0
    for i in obj:
        s += i
    return s

print("Suma elementów listy:",suma([2,34,5,5,3,3,345]))

#2. Napisz funkcję, która zwraca średnią elementów listy (krotki)
#3. Napisz funkcję, która sprawdza (zwraca true / false) czy z podanych długości odcinków można zbudować trójkąt
#4. Napisz funkcję, która sprawdza (zwraca true / false) czy liczba jest pierwsza

def prime(a):
    if a<2: return False
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return False
    return True

for i in range(1000):
    if prime(i) == True:
        print(i,end=", ")


#5a. Napisz funkcję, która oblicza NWD dwóch liczb
#5b. Napisz funkcję, która oblicza NWW dwóch liczb
#6. Napisz funkcję, która zwraca listę dzielników liczby (faktoryzacja).