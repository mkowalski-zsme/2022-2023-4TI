#Lista (List)
 
obj = [1,2,4,5,4,3,3,4,5,6,4,3,3]

print(obj)

'''
for i in obj:
    print(i)

i = 0
n = len(obj)
while i<n:
    print(obj[i])
    i+=1
'''
obj.append("DWA")  
obj.insert(1,3.5)  
obj.remove(3)
obj[2] = "ala ma kota"
print(obj)
print(obj[-2])

#Krotka (Tuple)
kr = (1,2,4,5,4,3,3,4,5,6,4,3,3)
print(kr)
'''
for i in kr:
    print(i)

i = 0
n = len(kr)
while i<n:
    print(kr[i])
    i+=1
'''
#kr[0] = "trzy" #błąd, nie można zmieniać zawartości krotki

#Zestaw (Set)

zest = {1,23,4,5,4,3,3,4,5,6,4,3,3}
print(zest)
zest.remove(1)
print(zest)
zest.add(123)
print(zest)

'''
for i in zest:
    print(i)
'''
'''
i = 0
n = len(zest)
while i<n:
    print(zest[i]) #błąd - nie można użyć notacji tablicowej
    i+=1
'''

#Słowniki (Dictionary)

dict = {"klucz":"wartość", "dzień":"piątek", 0:"zero", "0":"inne zero"}

print(dict)
print(dict["klucz"])
print(dict["dzień"])
print(dict[0])
print(dict["0"])
dict["marka"] = "bmw"
print(dict)

miesiace = {"styczeń":31,"luty":(28,29),"marzec":31}
for i in miesiace:
    print(i,miesiace[i])


