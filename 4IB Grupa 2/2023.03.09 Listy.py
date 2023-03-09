#Rozwiązanie zadania z kartkówki:
'''
a = float(input())
b = float(input())

if a > 0 and b > 0:
    print((a+b)/2)
'''
#########################

# Aane agregacyjne

# Lista (list)

lista1 = [1,2,4,5,3,2,4,"trzy"]
print(type(lista1))
print(lista1)

i = 0
n = len(lista1)
while i<n:
    print(lista1[i],end=",")
    i+=1
print("\n--------")

for i in lista1:
    print(i,end=",")
print("\n--------")

lista1.append(4.15)
lista1.insert(1,"ala ma kota")

for i in lista1:
    print(i,end=",")
print("\n--------")

lista1[5] = "aaaaa"
for i in lista1:
    print(i,end=",")
print("\n--------")

lista1.remove(2)

for i in lista1:
    print(i,end=",")
print("\n--------")

# Krotka (tuple)
print("---------- Krotka ----------")
krotka1 = (1,2,4,5,3,2,4,"trzy")
print(type(krotka1))
print(krotka1)

i = 0
n = len(krotka1)
while i<n:
    print(krotka1[i],end=",")
    i+=1
print("\n--------")

for i in krotka1:
    print(i,end=",")
print("\n--------")

#krotka1[5] = "aaaaa" #błąd krotka jest tylko do odczytu

# Zestaw (set)

print("---------- Zestaw ----------")
zestaw1 = {1,2,43,5,3,2,4,"trzy"}
print(type(zestaw1))
print(zestaw1)

'''
i = 0
n = len(zestaw1)
while i<n:
    print(zestaw1[i],end=",")
    i+=1
print("\n--------")
'''

for i in zestaw1:
    print(i,end=",")
print("\n--------")

zestaw1.add(10)
zestaw1.remove(2)
print(zestaw1)

# słownik (dict)

print("---------- Dziennik ----------")

slownik1 = {'klucz1': "wartość", "klucz2":123, "klucz3": (3,4,5,65)}
print(type(slownik1))
print(slownik1)

print(slownik1["klucz1"])
slownik1["nowy klucz"] = 333
slownik1[0] = 123
slownik1["0"] = 312

for i in slownik1:
    print(i, "->" ,slownik1[i])

rok = {"styczeń":31, "luty": (28,29), "marzec": 31}

print(rok)







