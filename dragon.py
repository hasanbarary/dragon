#!/usr/bin/python3.6
flag=1
square=int(input("Enter Side of the square --> "))
for i in range(0,square):
    print(" _",end="")
print("")
for i in range(0,square):
    for j in range(0,square+1):
        print("|",end="")
        if i==2 and j==5:
            print("X",end="")
        elif not j == square:
            print("_",end="")
    print("")
