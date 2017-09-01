import string

s=input("Enter the "-" seperated string")
sp=s.split("-")
print(sp)
q=sorted(sp)
print(q)
ans="-".join(q)
print(ans)