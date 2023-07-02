num = int(input("Enter a number: "))

if(num>0):
    print("Number is positive")
    if(num>10):
        print("Number is greater than 10")
    else:
        print("Number is less than 10")
elif(num==0):
    print("Number is equal to zero")
else:
    print("Number is negative")