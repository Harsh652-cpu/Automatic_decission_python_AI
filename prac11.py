#Program to test whether a number entered by the user is negative,positive or equal to zero
num=int(input("Enter any number:"))
if(num==0):
    print("The number "+str(num)+" is zero")
elif(num>0):
    print("The number "+str(num)+" is positive")
else:
    print("The number "+str(num)+" is negative")