#write a program to determine whether a person is eligible to vote or not.If not check how many years left to be eligible
age=int(input("Enter the age:"))
if(age>=18):
    print("You are eligible to vote")
else:
        yrs=18-age
        print("You have to wait for another "+str(yrs)+" years to be eligible to vote")
