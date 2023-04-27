class Osoba:
    def __init__(self,imie,nazwisko,wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    def __str__(self):
        return self.imie+" "+self.nazwisko+" "+str(self.wiek)
    
    def Wypisz(self):
        print(self.imie,self.nazwisko,self.wiek)



p1 = Osoba("Jan","Nowak",23)
p2 = Osoba("Anna","Kowalska",32)

print(p1,p2,sep="\n")

p1.Wypisz()
p2.Wypisz()



# print(p1.imie,p1.nazwisko,p1.wiek)
# p1.wiek = 33
# print(p1.imie,p1.nazwisko,p1.wiek)
# print(p2.imie,p2.nazwisko,p2.wiek)