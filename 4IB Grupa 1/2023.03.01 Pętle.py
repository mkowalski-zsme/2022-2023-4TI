i = -100
while i<100:
    print(i,end=",")
    i+=3

print("\n--------")

for i in range(-100,100,3):
    print(i,end=",")

print("\n--------")

for i in [2,3,5,3,2,4,5,3,2]:
    print(i,end=",")

print("\n--------")

for i in "jakis randomowy tekst":
    print(i,end=",")

print("\n--------")

#1. napisz program, który wypisuje n liczb na ekran (n podane z klawiatury)

n = int(input())

for i in range(n):
    print(i)

print("--------")

#2. napisz program, który oblicza sumę liczb z zakresu <a,b) (a i b podane z klawiatury)

a = int(input())
b = int(input())
s = 0

for i in range(a,b):
    s+=i
print(s)

print("--------")

#3. za pomocą pętli narysuj obszar o rozmiarze NxN zapełniony znakiami *

N = 10
i = 0
while i<N:
    j=0
    while j<N:
        print("*",end="")
        j+=1
    print()
    i+=1

print("--------")

#4. za pomocą pętli i instrukcji warunkowej narysuj litery: T, L, E, U, F N Z X 


N = 10
i = 0
while i<N:
    j=0
    while j<N:
        if j == N//2 or i==0: print("*",end="") #T
        else: print(" ",end="")
        j+=1
    print()
    i+=1

print("--------")
