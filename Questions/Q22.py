def disp(x):
    print("Val is ", x)


class abc:
    def __init__(self,val):
        self.val = val
    def disp(self):
        disp(self.val) #calling outer function
    def add_2(self):
        self.val+=2
        self.disp() #calling inner disp
obj=abc(10)
obj.add_2()
obj.add_2()
obj.add_2()
obj.add_2()

