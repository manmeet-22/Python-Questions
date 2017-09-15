s= 'string'
for i in s:
    x=ord(i)
    x=x-32
    j=chr(x)
    print(j)
p='STRING'
for j in p:
    y=ord(j)
    y=y+32
    j=chr(y)
    print(j)

print(dir(str))