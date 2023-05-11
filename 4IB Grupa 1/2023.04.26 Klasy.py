
class Pracownik:
    def __init__(self,imie,nazwisko,wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    
    def __str__(self):
        return self.imie +" "+self.nazwisko+" "+str(self.wiek)
    
    
    def Wiek(self):
        print(self.wiek)


osoba1 = Pracownik("Marcin","Nowak",23)
osoba2 = Pracownik("Anna","Jakaś",21)
print(osoba1)
print(osoba2)

# print(osoba1.imie, osoba1.nazwisko, osoba1.wiek)
# osoba1.wiek = 27
# print(osoba1.imie, osoba1.nazwisko, osoba1.wiek)
# print(osoba2.imie, osoba2.nazwisko, osoba2.wiek)

osoba1.Wiek()
