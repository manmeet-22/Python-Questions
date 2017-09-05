import re
pt=r"[0-9a-zA-Z]"
user ="manmeet22"
pan ="ABCD1234"
f=0
while(f==0):
    x=input("Enter 1 to input or 0 to exit")
    u = input("Enter username")
    p = input("Enter Pan card Number")
    if(x!=0):
        if(re.findall(pt,u) and re.findall(pt,u) ):
            if(u==user and p==pan):
                print("Login Successful")
            else:
                print("Login  Unsucessful")
    else:
        f=1