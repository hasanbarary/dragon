#!/usr/bin/python3.6
from random import randint
def show():
    for i in range(0,square):
        print(" _",end="")
    print("")
    for i in range(0,square):
        for j in range(0,square+1):
            print("|",end="")
            if j==x and i==y:
                print("X",end="")
            elif not j == square:
                print("_",end="")
        print("")
    print(x+1,y+1)
def up():
    if y != 0:
        return y-1
    else:
        print ("Where are you going !!? Your UP is the wall !")
        return y
def down():
    if y != square-1:
        return y+1
    else:
        print ("Where are you going !!? Your Down is the wall !")
        return y
def right():
    if x != square-1:
        return x+1
    else:
        print ("Where are you going !!? Your RIGHT is the wall !")
        return x
def left():
    if x != 0:
        return x-1
    else:
        print ("Where are you going !!? Your LEFT is the wall !")
        return x


square=int(input("Enter Side of the square --> "))
x=randint(0,square-1)
y=randint(0,square-1)
while True:
    show()
    answer=input("Enter your jahat --> ")
    if answer == 'u':
        y=up()
    elif answer == 'd':
        y=down()
    elif answer == 'r':
        x=right()
    elif answer == 'l':
        x=left()
    else:
        break
