x = int(input())

i = 0
while i<x:
    print(i)
    i+=1

print("---")

for i in range(x):
    print(i)

print("---")

for i in range(-10,100,x):
    print(i)

a = 3
b = 5
#operatory arytmetyczne
print(-a,+b)
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a%b)
print(a*b)
print(a**b)

#operatory tekstowe
a = "tekst1"
b = "tekst2"
print(a+b) #konkatenacja tekstów
print(a*3) #powielanie tekstu

#operatory relacji
print(a==b)
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a!=b)

#operator przypisania
a = 3
a += 2  #a = a + 2 
#itd...
