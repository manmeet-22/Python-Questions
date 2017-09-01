import string
s=input("Enter the string")
up=0
low=0
for i in s:
    if(i>='A' and i<='Z'):
        up+=1
    elif(i>='a' and i<='z'):
        low+=1
print("Uppercase = ",up)
print("Lowercase = ",low)
