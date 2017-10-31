print("enter the no.")
k = int(input())
p=k
c=0
while(p>0):
    n = p%10
    c = (c*10) + n
    p//=10
print(c)
if(c==k):
    print("no. is palintrom")
else:
    print("no. is not a palintrom")
