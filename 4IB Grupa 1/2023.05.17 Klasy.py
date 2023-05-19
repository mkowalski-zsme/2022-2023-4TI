class CUlamek:
    def __init__(self, licznik=0, mianownik=1):
        self.licznik = licznik
        if mianownik == 0:
            mianownik = 1
        self.mianownik = mianownik

    def __str__(self):
        return str(self.licznik)+" / "+str(self.mianownik)
    
    def value(self):
        if self.mianownik == 0: return "NaN"
        return self.licznik / self.mianownik


a = CUlamek(1,2)

a.mianownik = 0

print(a.licznik, a.mianownik)

print(a)
print(a.value())

