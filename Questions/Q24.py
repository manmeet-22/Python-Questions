class explode(str):
    def __init__(self,val = " "):
        str.__init__(self)
    def expl(self):
        if len(self) == 0:
            return self
        else:
            temp_str = ""
            blank_char = " "
            for i in range(0,len(self)-1):
                temp_str = temp_str + self[i]+blank_char
            temp_str = temp_str + self[len(self)-1]
        return temp_str

s = explode("Python")
print(s.expl())