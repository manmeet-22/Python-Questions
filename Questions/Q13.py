import re

pt=r"\b\w"
pt=r"\w"
st="Python - + = aaaa bbb ccc"
res=re.findall(pt,st)
print(res)
'''ans=[]
for i in res:
    if i not in ans:
        ans.append(i)
print(ans)'''