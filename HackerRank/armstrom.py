print("enter the no\n")
c = int(input())
k=c
i=0
j=0
su=0
while(k>0):
    i = (k%10)
    su += i**3
    k //= 10

if(c==su):
    print(c," is arstrom \n")

else:
    print(c," is not arstrom no.\n")
