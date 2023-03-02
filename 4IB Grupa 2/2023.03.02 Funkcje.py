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
