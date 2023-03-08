#rozwiązanie z kartkówki:
'''
a = input("Podaj 1 liczbę ")
b = input("Podaj 1 liczbę ")

if float(a) > float(b):
    print(a)
else:
    print(b)
'''
#funkcje w Python:


#Wywołanie funkcji:

print()


# definicja funkcji Hello():
def Hello():
    print("Hello")

Hello()

# redefinicja funkcji Hello(arg):

def Hello(imie):
    print("Hello",imie)

Hello("Marcin")

def Suma(a,b):
    return a+b

x = Suma(3,4)
print(x)

print(Suma(5,7)) #12 wynik dodawania
print(Suma("5","7")) #57 wynik konkatenacji (złączenia tekstów)
#print(Suma(5,"7")) # błąd dodawania
#print(Suma("5",7)) # bład konkatenacji

def Dziel(a,b):
    if b != 0:
        return a/b
    else:
        if a>0: return "Inf"
        elif a<0: return "-Inf"
        else: return "NaN"
    

print(Dziel(3,0))
print(Dziel(-3,0))
print(Dziel(0,0))
print(Dziel(3,4))

#1. Zdefinuj funkcję, która wyświetla powitalny tekst dla osoby podanej jako argument
#2. Zdefinuj funkcję, która przyjmuje dwa liczby i wypisuje większą z nich
#3. Zdefinuj funkcję, która sprawdza czy z podanych długości odcinków można zbudować trójkąt i zwraca True/False
#4. Zdefinuj funkcję, która sprawdza czy podana liczba jest pierwsza (True/False)

