class abc:
    class_var = 0
    sal=0
    name=""
    dept=0
    def disp(self):
        print(self.name ,self.sal, self.dept )
    def total(self): return abc.class_var
    def __init__(self,name,sal,dept):
        abc.class_var+=1
        self.name = name
        self.sal = sal
        self.dept = dept
obj1=abc("A",10,"a")
obj2=abc("B",20,"b")
obj3=abc("C",30,"b")
obj4=abc("D",40,"b")
obj1.disp()
obj2.disp()
obj3.disp()
obj4.disp()

print("The number of employees are ",obj4.total())
