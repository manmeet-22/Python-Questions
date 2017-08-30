hpr= float(input("Enter Hourly pay rate"))
hw= float(input("Enter Hours worked "))
pws= float(input("Enter Percentage withheld salary"))
gross=0
if hw>40 :
    extra = hw-40;
    gross=(extra*1.5*hpr)+ (hpr*40)
else:
    gross= hpr * hw #Calculating gross salary
with_held_sal = gross * (pws/100) #Calculating withheld salary
net_pay = gross - with_held_sal #Calculating net amount

print("The net pay is " ,net_pay)