
#Rozwiązanie zadania z kartkówki:
'''
a = int(input())
b = int(input())

if a % 2 == 0 or b % 2 == 0:
    print(a+b)
'''

#1. Napisz funkcję, która zwraca sumę elementów listy (krotki)

def suma(arg):
    pass

#2. Napisz funkcję, która zwraca średnią elementów listy (krotki)
#3. Napisz funkcję, która sprawdza (zwraca true / false) czy z podanych długości odcinków można zbudować trójkąt
#4. Napisz funkcję, która sprawdza (zwraca true / false) czy liczba jest pierwsza

def Pierwsza(liczba):
    if liczba < 2: return False
    for i in range(2,int(liczba**.5)+1):  # range zwraca zakres <2, liczba)
        if liczba % i == 0: return False

    return True

for i in range(100):
    print(i, "->", Pierwsza(i))


lista_p = [i for i in range(1000) if Pierwsza(i)]
print(lista_p)

#5a. Napisz funkcję, która oblicza NWD dwóch liczb

def NWD(a,b):
    while a!=b:
        if a>b: 
            a -= b
        else:
            b -= a
    return a

print (NWD(3,5))
print (NWD(3,15))

#5b. Napisz funkcję, która oblicza NWW dwóch liczb

def NWW(a,b):
    return a*b//NWD(a,b)

print (NWW(3,5))
print (NWW(3,15))

#6. Napisz funkcję, która zwraca listę dzielników liczby (faktoryzacja).

def faktoryzacja(liczba):
    r = []

    return r

"""
faktoryzacja(5) -> [5]
faktoryzacja(15) -> [3,5]
faktoryzacja(20) -> [2,2,5]
faktoryzacja(25) -> [5,5]

"""