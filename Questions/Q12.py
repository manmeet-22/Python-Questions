import re

'''
pt=r"(.)+"
st="Python - + = aaaa"
x=[]
#match = re.search(pt,st)
#print(match)
for i in st:
    x.append(re.findall(pt,i))
ans=[]
for i in x:
    if i not in ans:
        ans.append(i)
print(ans)
'''

pt=r"."
st="Python - + = aaaa"
res=re.findall(pt,st)
print(res)
ans=[]
for i in res:
    if i not in ans:
        ans.append(i)
print(ans)