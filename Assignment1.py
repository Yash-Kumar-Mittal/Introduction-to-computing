#Question 1
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Num3 = int(input("Enter the third number: "))
Avg = (Num1 + Num2 + Num3)/3
print("Average of the numbers is: ",Avg)


#Question 2

income = float(input("Enter your gross income: "))
dependants = int(input("No. of dependants: "))
deduction = 10000
deduction_per_dependant = 3000
charge = 1/5                   #charge = 20%

taxable_income = income - deduction - (deduction_per_dependant * dependants)

tax = float(taxable_income * charge)

print("Total income tax you have to pay is: ",tax)




#Question 3
Student = [21105069, 'Yash Kumar Mittal', 'M', 'ECE', 9.82]
print(Student)





#Question 4
Marks1 = float(input("Enter the marks of student 1: "))
Marks2 = float(input("Enter the marks of student 2: "))
Marks3 = float(input("Enter the marks of student 3: "))
Marks4 = float(input("Enter the marks of student 4: "))
Marks5 = float(input("Enter the marks of student 5: "))
Marks_List = [Marks1,Marks2,Marks3,Marks4,Marks5]
print("List before sorting: ",Marks_List)
Marks_List.sort()
print("List after sorting: ",Marks_List)




#Question 5 (a)
color = [ 'Red','Green','White','Black','Pink','Yellow' ]
color.pop(3)
print(color)


#Question 5 (b)
color = [ 'Red','Green','White','Black','Pink','Yellow' ]
color[3:5]=["Purple"]
print(color)




























