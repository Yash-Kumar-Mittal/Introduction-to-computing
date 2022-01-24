#QUESTION-1


Str = "Python is a case sensitive language"
print("The length of string is : ",len(Str))                     

Reversed_Str = Str[ : : -1]
print("The reversed string is : ",Reversed_Str)                     

new_Str = Str[10:26]
print("The new string is : ",new_Str)

replaced_str= Str.replace( 'a case sensitive','object oriented')     
print ("The replaced string is : ",replaced_str)

index = Str.find('a')  
if (index == -1):
    print(" String does not contain the substring 'a' ")           
else :                                               
    print("The index of 'a' in the given String is : ",index)            

Strwithoutspace = Str.replace(" ","")
print("The given string without white spaces is : ",Strwithoutspace)    #Printing the string without white spaces


#QUESTION-2


Name = input("Enter your Name : ")
SID = int(input("Enter your SID : "))
Dept_Name = input("Enter your Department name : ")
CGPA = float(input("Enter your CGPA : "))

print('''
Hey, %s Here!
My SID is %d
I am from %s department and my CGPA is %.1f''' %(Name,SID,Dept_Name,CGPA))


#QUESTION-3


a=56
b=10
print("Value of a & b is : ", (a & b))						
print("Value of a | b is : ", (a | b))						
print("Value of a ^ b is : ", (a ^ b))						
print("Left shift both a and b with 2 bits : ", (a<<2, b<<2))		
print("Right shift a with 2 bits and b with 4 bits : ", (a>>2, b>>4))	


#QUESTION-4

Num1= int(input("Enter the first number : "))
Num2= int(input("Enter the second number : "))
Num3= int(input("Enter the third number : "))

if ((Num1 > Num2) and (Num1 > Num3)):
    print("The greatest of the three numbers is : ", Num1)

elif ((Num2 > Num1) and (Num2 > Num3)) :
    print("The greatest of the three numbers is : ", Num2)

else :
    print("The greatest of the three numbers is : ",Num3)   #If above conditions dosen't satisfy then it's clear that num3 must be greatest




#QUESTION-5

str = input("Enter the String : ")          

if "name" in str :			
    print("Yes")
else :
    print("No")



#QUESTION-6

len1 =float(input("Enter the length of first side of triangle : "))
len2 =float(input("Enter the length of second side of triangle : "))
len3 =float(input("Enter the length of third side of triangle : "))

#CONVERTING THE LENGTH INTO INTEGER
len1=int(len1)
len2=int(len2)
len3=int(len3)

if ( (len1 > len2+len3) or (len2 > len1+len3) or (len3 > len1+len2)) :  
    print ("No")

else :
    print ("Yes")


















