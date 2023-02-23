#pętla while

i=0
while i<100:
    print(i)
    i+=1

print("----------")

#pętla for in
for i in range(100):
    print(i)

print("----------")

for i in range(30,100,13):  #generuje zestaw liczba od 30 do 99 co 13
    print(i)

#przykład z lekcji

x = int(input("Podaj liczbę: "))
print("Podana liczba (",x,") jest:")
if x<0:
    print("ujemna,",end=" ")
elif x>0:
    print("dodania,",end=" ")
else:
    print("równa zero,",end=" ")

if x%2 == 0:
    print("parzysta,",end=" ")
else:
    print("nieparzysta,",end=" ")

if x>1:
    i = 2
    f = True
    while i*i<=x:
        if x % i == 0:
            f = False
            break
        i+=1

    if f:
        print("pierwsza")
    else:
        print("złożona")

