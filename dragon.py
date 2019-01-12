#!/usr/bin/python3.6
from random import randint
import os
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
#    print(x+1,y+1)
#    print(dragonx+1,dragony+1)
#    print(doorx+1,doory+1)
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
def rand():
       return  randint(0,square-1)
square=int(input("Enter Side of the square  >>> "))
dragonx=rand()
dragony=rand()
doorx=rand()
doory=rand()
x=rand()
y=rand()
while True:
    os.system('clear')
    show()
    if x==dragonx and y==dragony:
        print("Game Over,Try again")
        break
    if x==doorx and y==doory:
        print("congratulation,You are the Best")
        break   
    answer=input("Enter your direction \n'r' for right \n'l' for left \n'u' for up \n'd' for down \n --> ").lower()
    if answer == 'u' or answer == 'up':
        y=up()
    elif answer == 'd' or answer == 'down':
        y=down()
    elif answer == 'r' or answer == 'right':
        x=right()
    elif answer == 'l' or answer == 'left':
        x=left()
    else:
        break
