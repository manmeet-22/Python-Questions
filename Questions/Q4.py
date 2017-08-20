f=1
while(f==1) :
    x= float(input("Enter First Number"))
    y = float(input("Enter Second Number"))
    choice = input("Enter \na. + for Addition\nb. - for Subtract\nc. * for Multiply\nd. / for Divide\ne. % for Remainder\nf. X for exit\n")
    if (choice == '+') :
        ans = x+y
    elif (choice == '-') :
        ans= x-y
    elif (choice == '*'):
        ans = x * y
    elif (choice == '/'):
        ans = x / y
    elif (choice == '%') :
        ans= x%y
    elif (choice == 'X') :
        f=0
    else :
        print("Invalid input")

    print(ans)