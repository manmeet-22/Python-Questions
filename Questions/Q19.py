#!/bin/python

import sys
import os


# Complete the function below.s

def makefrom():
    x=input()
    y=x.upper()
    x=x[2:]
    y=y[:len(y)-2]
    print(x,y)
    d={k:v for k,v in zip(y,x)}
    print(d)

if __name__ == "__main__":
    res = makefrom();

