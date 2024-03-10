import sys
import math
import random
A=[1-x for x in range(1,11)]
B=[4**y for y in range(0,8)]
C=[x for x in B if x%2==0]
print(A)
print(B)
print(C)
l1=random.sample(range(1,100),10)
l2=[x for x in l1 if x%2==0]
print(l1)
print(l2)
s1={'hotwheels':'sztuki','jajka':'sztuki','ser':'kg','mleko':'l'}
s2={k:v for k,v in s1.items() if v=='sztuki'}
print(s1)
print(s2)
def pitagoras(a,b,c):
    if c**2==a**2+b**2:
        return 'jest prostokatny'
    else:
        return'nie jest prostokatny'
print(pitagoras(3,4,5))
def pole_trapezu(a=3,b=4,h=7):
    pole=((a+b)*h)/2
    return pole
print(pole_trapezu())
def iloczyn(a=1,b=4,ile=10):
    wynik=1
    a1=a
    for j in range(a,ile+1):
        wynik*=a1
        a1+=b
    return wynik
print(iloczyn())
try:
    liczba=int(input('Podaj liczbe: '))
    pierwiastek=math.sqrt(liczba)
except ValueError:
    print('Error!')
else:
    print(pierwiastek)



