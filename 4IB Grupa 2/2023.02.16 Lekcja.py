
a = input("Podaj liczbę a: ") #lub od razu a = int(input("Podaj liczbę a: "))
a = int(a)

#instrukcja warunkowa
if a > 0:
    print("Liczba dodatnia")
elif a<0:
    print("Liczba ujemna")
else:
    print("Liczba zero")

#pętla while
i=0
while(i<100):
    print(i,end=", ")
    i = i + 1   # i += 1
print()

#pętla for..in
for i in range(100):    #wypisanie elementów zakresu <0,100)
    print(i)








