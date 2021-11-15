#write a program that prompts the user to enter a number between 1-7(1 to 7) and then displays the corresponding day of the week
num=int(input("Enter the number(between 1 to 7):"))
if(num==1): print("Sunday")
elif(num==2): print("Monday")
elif(num==3): print("Tuesday")
elif(num==4): print("Wednessday")
elif(num==5): print("Thurday")
elif(num==6): print("Friday")
elif(num==7): print("Saturday")
else:
    print("Wrong input,please input the values between 1 and 7(including 1 and 7)")