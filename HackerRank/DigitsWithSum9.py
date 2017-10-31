def sum9(n):
    a=(n/900)
    b=10-(n/90-a*10)
    a=10-a
    sum1=0
    count=0
    for i in range(a+1):
        count+=i
        sum1+=count
    c=220-sum1
    sum1=0
    for i in range(a,b,-1):
        sum1+=i
    c=c+sum1
    
    z=((10-a)*90+(10-b)*9)
    a=n/10
    for i in range(z,a):
        b=i/1000+(i/100-(i/1000)*10)+(i/10-i/100*10)+(i%10)
        if b<=9:
            c+=1
    i+=1
    b=i/1000+(i/100-(i/1000)*10)+(i/10-i/100*10)+(i%10)
    if b<=9:
        b=9-b
        if b<=n%10:
            c+=1
    return c
n=int(input('enter the digit'))
devil9= sum9(n)
print devil9
