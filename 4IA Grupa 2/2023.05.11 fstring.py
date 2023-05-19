for i in range(1,10):
   #print("Liczba nr " + str(i))
    print(f"Liczba nr {i}")

zmienna = "ala ma kota"

print(zmienna[::-1])
print(zmienna[1:10:1])
print(zmienna[2:9:2])

l = ['1','2','3','4']
f = [1,2,3,4,5,7]
f = [str(i) for i in f]

s = "".join(f)
print(s)