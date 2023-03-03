#funkcje
#defeinicja funkcji Hello
def Hello():
    print("Hello") 

Hello()


#redefeinicja funkcji Hello
def Hello(imie):
    print("Hello",imie)

Hello("Marcin")
Hello("Jan")

"""
#wyrażenie warunkowe w C++
int y = 5;
int x = y > 3 ? 5 : 7;

"""


#zwracanie wartości

def Suma(a,b):
    print("Sumowanie dwóch argumentów:",a,"i",b)
    return a+b


x = Suma(3,4)
print(x)
print(Suma("3","4"))
#print(Suma("3",4)) błąd konkatenacji
#print(Suma(3,"4")) bład dodawania liczb

def Dziel(a,b):
    a = float(a)
    b = float(b)
    if b!=0: return a / b
    return "Inf"

print(Dziel(3,0))
print(Dziel(3,4))