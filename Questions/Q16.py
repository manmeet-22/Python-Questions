t={'a': "Hello! " ,'b': "How ", 'c': "are ", 'd': "you ", 'e' :"?"}
i=1
x ={}
for k,v in t.items():
    if(i%2 == 0):
        temp = t[k]
        t[k] = t[x]
        t[x] = temp
    i+=1
    x = k

for k,v in t.items():
    print(t[k])

print(t.items())

