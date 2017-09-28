class abc:
    def __init__(self,val):
        self.val = val
    def disp(self):
        disp(self.val) #calling outer function
    def add_2(self):
        self.val+=2
        self.disp() #calling inner disp

name = ""
m=[]
while(1):
    name = input("Enter Name")
    if(name=='-1'):
        break
    for i in range(0,3):
        m[i] = int(input("Enter sub"+str(i)+" marks"))
