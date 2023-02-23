a = 3
print(a,type(a)) #liczba całkowita
a = 3.5
print(a,type(a)) #liczba zmiennoprzecinkowa
a = "3"
print(a,type(a)) #tekst
a = True
print(a,type(a)) #wartość logiczna
a = (-1)**0.5
print(a,type(a)) #liczba zespolona

a = int(input("Podaj wartość: "))
print(a,type(a))

if a>0:
    print("liczba dodatnia")
elif a<0:
    print("liczba ujemna")
else:
    print("liczba 0")
