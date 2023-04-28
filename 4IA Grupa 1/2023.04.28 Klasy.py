#Klasy w Python

class Osoba:
    def __init__(self,imie,nazwisko,wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def Wypisz(self):
        print(self.imie,self.nazwisko, self.wiek)

    def __str__(self):
        # return self.imie+" "+self.nazwisko+" "+str(self.wiek)
        return f"{self.imie} {self.nazwisko} {self.wiek}"
    

p1 = Osoba("Jan","Kowalski",32)
p2 = Osoba("Anna","Nowak",23)

print(p1)
print(p2)

# print(p1.imie, p1.nazwisko, p1.wiek)
p1.Wypisz()
p2.Wypisz()

# for k,w in p1.__dict__.items():
#     print(k,w)

# baza = [Osoba("Jan","Kowalski",32), Osoba("Anna","Nowak",23)]

# for el in baza:
#     el.Wypisz()

# a = 3
# b = True
# c = "tekst"

# print(f" {a} {b} {c}")