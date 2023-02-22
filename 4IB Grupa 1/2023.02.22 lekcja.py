a = 123
print(a,type(a))
a = 3.14
print(a,type(a))
a = "123"
print(a,type(a))
a = True
print(a,type(a))
a = 123 + 7j
print(a,type(a))

a = input("Podaj liczbę: ") #funkcja input zwraca string

a = int(a) #konwersja na int

print(a,type(a))

if a < 0:
    print("Liczba ujemna")
elif a>0:
    print("Liczba dodatnia")
else:
    print("Liczba zero")