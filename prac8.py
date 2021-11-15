#A company decides to give bonus to all its employes on Diwali.A 5% bonus on salary is given to the male workers and 10%
#bonus on salary to the female workers.Write a program to enter the salary of the employee and sex of the employee.
#If the salary of the employee is less than Rs 10,000 then the employee gets an extra 2% bonus on the salary.
#Calculate the bonus that has to be given to the employee and display the salary that the employee will get.
salary=float(input("Enter the salary of the employee:"))
sex=input("Enter you gender(M or F):")
male_sal=(salary*0.05)+salary 
female_sal=(salary*0.10)+salary
if(salary>10000.00):
    if(sex=='M'):
     print(str("%.2f"%male_sal))
    elif(sex=="F"):
     print(str("%.2f"%female_sal))
else:
    male_sala=(male_sal*0.02)+male_sal
    female_sala=(female_sal*0.02)+female_sal
    if(sex=='M'):
     print(str("%.2f"%male_sala))
    elif(sex=='F'):
     print(str("%.2f"%female_sala))
    
    


    