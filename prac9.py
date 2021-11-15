#Program to find whether a given year is a leap year or not
year=int(input("Enter the year you want to check:"))
if(year%4==0 and year%100!=0) or (year%400==0):
    print("Leap Year")
else:
    print("Not a leap year")
