#!/usr/bin/python3.6
from random import randint
square=int(input("Enter Side of the square --> "))
for i in range(0,square):
    print(" _",end="")
print("")
x=randint(0,square-1)
y=randint(0,square-1)
for i in range(0,square):
    for j in range(0,square+1):
        print("|",end="")
        if i==x and j==y:
            print("X",end="")
        elif not j == square:
            print("_",end="")
    print("")
print(x+1,y+1)
