"""
Instrukcja warunkowa w C++

x = 3
y = x > 3 ? 5 : 10;

"""
#definicja funkcji

def Hello():
    print("Hello")

def Hello2(imie):
    print("Hello",imie)

def Suma(a,b):
    return float(a)+float(b) #konwersja argumentów na float

def Dziel(a,b):
    a = float(a)
    b = float(b)
    if b!=0: return a / b
    return "Inf"

def SumaEl(arg):
    s = 0
    for i in arg:
        s+= i
    return s

Hello()
Hello2("Marcin")

print(Suma(3,4))
print(Suma(3,"4")) 

print(Dziel(3,4))
print(Dziel(3,0))

print(SumaEl([2,3,4,65,4,3,4,5,6]))


#1. Zdefinuj funkcję, która liczy sumę dwóch liczb
def Sum(a,b):
    return float(a) + float(b)

#2. Zdefinuj funkcję, która sprawdza znak liczby i wypisuje odpowiednią informację na ekran
def Sign(a):
    if a>0: print("Dodatnia")
    elif a<0: print("Ujemna")
    else: print("Zero")

#3. Zdefinuj funkcję, która sprawdza czy z podanych długości odcinków można utworzyć trójkąt (False/True)
def Triangle(a,b,c):
    if a>b+c and b>a+c and c>a+b: return True
    else: return False

#4. Zdefinuj funkcję, która sprawdza czy podana liczba jest pierwsza
def Prime(a):
    if a<2: return False
    for i in range(2, int((a**.5)+1)):
        if a%i == 0: return False
    return True

for i in range(100):
    print(i,Prime(i))

#5. Zdefinuj funkcję, która zwraca NWD dwóch liczb
def NWD(a,b):
    while(a!=b):
        if a>b: a-=b
        else: b-=a
    return a

print(NWD(5,5))

def NWD2(a,b):
    while True:
        r = a%b
        if r == 0: return b
        else: 
            a=b
            b=r
    return b

print(NWD2(51,15))
