#program to find the greatest number out of three numbers
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if(num1>num2 and num1>num3):
    print(str(num1)+" is greatest out of "+str(num2)+" and "+str(num3))
elif(num2>num1 and num2>num3):
    print(str(num2)+" is greatest out of "+str(num1)+" and "+str(num3))
else:
    print(str(num3)+" is greatest out of "+str(num2)+" and "+str(num1))