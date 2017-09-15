#!/bin/python

import sys
import os


# Complete the function below.

def remove_dup(i1, i2):
    x=i1
    for i in i2:
        x=x.replace(i,'9')
    for i in x:
        if(i!="9"):
            print(i,end="")



if __name__ == "__main__":
    try:
        inputstr1 = input()
    except:
        inputstr1 = None

    try:
        inputstr2 = input()
    except:
        inputstr2 = None

    res = remove_dup(inputstr1, inputstr2);
