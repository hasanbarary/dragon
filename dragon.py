#!/usr/bin/python3.6
flag=1
for i in range(0,10):
    print(" _",end="")
print("")
for i in range(0,10):
    for j in range(0,11):
        print("|",end="")
        if i==2 and j==5:
            print("X",end="")
        elif not j == 10:
            print("_",end="")
    print("")
