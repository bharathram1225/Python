while True:
    print("1. Addition")
    print("2. Substration")
    print("3. Multiplication")
    print("4. division")
    print("5. floor division")
    print("6. power")
    print("7. equal to operator ==")
    print("8. less than equal to <=")
    print("9. Greater than equal to >=")
    print("10. not equal to !=")
    print("11. left shift <<")
    print("12. right shift >>")
    print("13. not operator ~")

    
    chooice=int(input("enter the chooice "))

    if chooice == 1:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        c=a+b
        print("The value of the %f and %f is %f"%(a,b,c))

    elif chooice == 2:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        c=a-b
        print("The value of the %f and %f is %f"%(a,b,c))

    elif chooice == 3:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        c=a*b
        print("The value of the %f and %f is %f"%(a,b,c))

    elif chooice == 4:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        c=a/b
        print("The value of the %f and %f is %f"%(a,b,c))

    elif chooice == 5:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        c=a//b
        print("The value of the %f and %f is %f"%(a,b,c))

    elif chooice == 6:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        c=a^b
        print("The value of the %f and %f is %f"%(a,b,c))

    elif chooice == 7:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        if a == b:
            print("The value of the %f and %f are equal")
        else:
            print("The value of the %f and %f are not equal")

    elif chooice == 8:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        if a <= b:
            print("The value %f is less than or equal to %f ")
        else:
            print("The value %f is greater than or equal to %f ")

    elif chooice == 9:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        if a >= b:
            print("The value %f is greater than or equal to %f ")
        else:
            print("The value %f is less than or equal to %f ")

    elif chooice == 10:
        a=float(input("Enter the first integer or float value a :"))
        b=float(input("Enter the first integer or float value b :"))
        if a != b:
            print("The value %f is not equal to %f ")
        else:
            print("The value %f is equal t to %f ")

    elif chooice == 11:
        a=int(input("Enter the first integer or float value a :"))
        n=int(input("Enter the number of times you want to do left shift n :"))
        a>>n
        print(" the left shift of ",a," of ",n,"times is ",a<<n)

    elif chooice == 12:
        a=int(input("Enter the first integer or float value a :"))
        n=int(input("Enter the number of times you want to do left shift n :"))
        a>>n
        print(" the right shift of ",a," of ",n,"times is ",a>>n)

    elif chooice == 13:
        a=int(input("Enter the first integer or float value a :"))
        b=int(input("Enter the first integer or float value b :"))
        
        print(" a XOR b is :",a^b)

    else:
        print("entered the valid choice")
              
        
                    
            
        
    
    
