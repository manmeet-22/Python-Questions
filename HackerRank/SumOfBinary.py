a = input()
b = input()
res = ""
rem = 0
while a!=0 or b!=0:
    res += str((a%10 + b%10 + rem)%2)
    rem += (a%10 + b%10 + rem)/2
    a = a/10
    b = b/10
if rem:
    if(res.count("1") == 1):
        res = "0" + res
    else:
        res = "1" + res
print res[::-1]
