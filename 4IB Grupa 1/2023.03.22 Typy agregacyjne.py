#Listy (list)

# ob1 = [2,3,5,5,6,3,4,"tekst",3.4]

# print(ob1)

# # i = 0
# # n = len(ob1)
# # while i<n:
# #     print(ob1[i])
# #     i+=1

# ob1.append(123)
# ob1.insert(1,"ala ma kota")
# ob1.remove(3)
# ob1[0] = "nowa wartość"

# for el in ob1:
#     print(el)


#krotka (tuple)

# ob2 = (2,3,5,5,6,3,4,"tekst",3.4)
# print(ob2)

# # i = 0
# # n = len(ob2)
# # while i<n:
# #     print(ob2[i])
# #     i+=1

# for el in ob2:
#     print(el)

#zestaw (set)

# ob3 = {2,3,5,5,6,3,4,"tekst",3.4}
# print(ob3)

# # i = 0
# # n = len(ob3)
# # while i<n:
# #     print(ob3[i]) #błąd
# #     i+=1


# ob3.remove(6)
# ob3.add(7)

# for el in ob3:
#     print(el)


#słownik (dict)

ob4 = {0: 4, "klucz": "wartość", "0": "inna wartość"}

print(ob4)

ob4["0"] = 123

ob4["test"] = 4312
for klucz in ob4:
    print(klucz, ob4[klucz])
