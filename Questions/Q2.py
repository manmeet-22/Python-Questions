n= float(input("Enter Temperature"))
choice = int(input("Enter \na. 1 for Farnheit -> Celcius\nb. 2 for  Celcius -> Farnheit"))
if (choice == 1) :
    c = (n - 32)*5/9;
    print("Farnheit -> Celcius is ", c)
elif (choice == 2) :
    f = (n * 9/5) +32;
    print("Celcius->Farnheit is ", f)
