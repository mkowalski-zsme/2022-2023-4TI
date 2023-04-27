class Osoba:
   
    def __init__(self,imie,nazwisko,wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def __str__(self):
        # return self.imie+" "+self.nazwisko+" "+str(self.wiek)
        return f"{self.imie} {self.nazwisko} {self.wiek}"
    

    def Wypisz(self):
        # print(self.imie+" "+self.nazwisko+" "+str(self.wiek))
        print(f"{self.imie} {self.nazwisko} {self.wiek}")

    def Test():
        print("test")



ob1 = Osoba("Marcin","Nowak",23)
ob2 = Osoba("Kasia","Kowalska",43)

# ob1.wiek = -12

# print(ob1.imie, ob1.nazwisko, ob1.wiek)
# print(ob1)
# print(ob2)
# ob1.Wypisz()
# ob2.Wypisz()


# for i,j in ob1.__dict__.items():
#     print(f"{i}: {j}")

dane = []
dane.append(Osoba("Marcin","Nowak",23))
dane.append(Osoba("Kasia","Kowalska",43))
# lub
dane = [Osoba("Marcin","Nowak",13),Osoba("Adam","Nowak",43),Osoba("Romek","Nowak",23)]

for i in dane:
    print(i)

Osoba.Test()





