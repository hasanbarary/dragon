#!/usr/bin/python3.6
from random import randint
import os
import sys
import tty, termios
def print_help():
    print("\n          w:(UP)      \na:(LEFT)         d:(RIGHT)\n         s:(DOWN)\n\nq:EXIT\n\n>>> ")
def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

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
os.system('clear')
square=int(input("Enter Side of the square  >>> "))
dragonx=rand()
dragony=rand()
doorx=rand()
doory=rand()
x=rand()
y=rand()
while True:
    show()
    if x==dragonx and y==dragony:
        print("Game Over,Try again")
        break
    if x==doorx and y==doory:
        print("congratulation,You are the Best")
        break  
    print_help()
#    answer=input("Enter your direction \n'r' for right \n'l' for left \n'u' for up \n'd' for down \n --> ").lower()
#    print("Enter your direction \n'd' for RIGHT \n'a' for LEFT \n'w' for UP \n's' for DOWN \n'q' for EXIT\n >>> ")
    answer=getch()
    if  answer == 'w':
        y=up()
    elif  answer == 's':
        y=down()
    elif  answer == 'd':
        x=right()
    elif  answer == 'a':
        x=left()
    elif answer == 'q':
        break
    else:
        os.system('clear')
        print("Just Enter UP:'u'or'w'  DOWN:'d'or's' RIGHT:'r'or'd' LEFT:'l'or'a'")
        continue
    os.system('clear')

