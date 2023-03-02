#
def Hello():
    print("Hello")

Hello()

def Hello(arg):
    print("Hello",arg)

Hello("Marcin")

def Suma(a,b):
    return a+b

x = Suma(3,4)
print(x)

print(Suma(4,5))

print(Suma("4","5"))

#print(Suma("4",5)) #błąd konkatenacji
 
#print(Suma(4,"5")) #błąd dodawania

def Dziel(a,b):
    a = float(a)
    b = float(b)
    if b == 0:
        return "Inf"
    return a / b

print(Dziel(3,0))
print(Dziel(3,4))
