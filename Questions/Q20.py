class abc:
    class_var = 0;
    def disp(self):
        return abc.class_var
    def __init__(self):
        abc.class_var+=1
obj=abc()
obj=abc()
obj=abc()
obj=abc()

print("The value of val is ",obj.disp())
