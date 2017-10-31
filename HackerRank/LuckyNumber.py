#!/bin/python3

import sys

def onceInATram(x):
    flag=0
    while(flag!=1):
        x = str(x)
        one = int(x[:1])+int(x[1:2])+int(x[2:3])
        x = int(x)
        x +=1
        x = str(x)
        two = int(x[3:4])+int(x[4:5])+int(x[5:6])


        if(one == two):
            return int(x)


if __name__ == "__main__":
    x = raw_input()
    result = onceInATram(x)
    print(result)
