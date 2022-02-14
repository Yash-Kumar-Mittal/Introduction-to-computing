#Question 1

print("Question 1") 
#taking input from user
text = input("Enter the text:\n")
text=text.lower().strip() 
i=0
#defining an empty dictionary to use later to store element, counter pairs and removing common letters and words
dict={}

#checking if the text input is a word or a sentence
if " " not in text:
     #searching for common characters
     while i<len(text):
          counter=0
          j=0
          while j<len(text):
               if text[i]==text[j]:
                    counter=counter+1
                    j=j+1
               else:
                    j=j+1
          #storing the values in dictionary
          dict[f"{text[i]}"]=counter
          i=i+1

else:
     #making a list of words using split method
     list = str.split(text)
     #searching for common words
     while i<len(list):
          counter=0
          j=0
          while j<len(list):
               if list[i]==list[j]:
                    counter=counter+1
                    j=j+1
               else:
                    j=j+1
                    #storing the pairs in dictionary 
          dict[f"{list[i]}"]=counter 
          i=i+1
#Printing the final result
print("Total occurances")
for key,value in dict.items():
    print(f"The occurence of {key} in the given text is {value}")  
********************************************************************************

# Question2

print("Question 2")

#Taking input from the user
day=int(input("Enter the Day- ")) 
month=int(input("Enter the Month- ")) 
year=int(input("Enter the Year- "))


#Removing all the invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif day==30 and month==2 and year%4==0: 
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0: 
    condition=False
else:
    condition=True


#After checking the condition, following if-else statement is executed
if condition:
    #checking and changing for new year and new month
    if day==31 and month==12:
        next_year=year+1
    else:
        next_year=year
    if month==12 and day==31: 
        next_month=1
    else:
        next_month=month
#changing dates
    #checking for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1 
            if month!=12:
                next_month=month+1
            else:
                next_month=1 
        else:
            next_day=day+1
    #checking for the month of february
    elif month==2:
        if year%4==0:
            if day==29:
                next_day=1
                next_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
                next_month=3
            else:
                next_day=day+1
                    
    #Covering all the remaining cases
    else:
        if day==30:
            next_day=1
            next_month=month+1
        else:
            next_day=day+1
    #Printing the Final date
    print(f"Next Date is: {next_day}/{next_month}/{next_year}")
else:
    #if invalid date then give indication to user
    print("This is not a valid date") 
******************************************************************

# Question3

print("Question 3") 


list1 = [4,5,6,9]
print(list1) 

list2 = []
for x in list1:
    tuple = (x,x**2)
    list2.append(tuple)
print(list2)
******************************************************************

#Question 4

print("Question 4")
grade=int(input("Enter the grade points:\n")) 

dict={10:{'Letter_Grade':'A+','Performance':'Outstanding'},
           9:{'Letter_Grade':'A','Performance':'Excellent'},
           8:{'Letter_Grade':'B+','Performance':'Very Good'},
           7:{'Letter_Grade':'B','Performance':'Good'},
           6:{'Letter_Grade':'C+','Performance':'Average'},
           5:{'Letter_Grade':'C','Performance':'Below Average'},
           4:{'Letter_Grade':'D','Performance':'Poor'}}
if (4<=grade<=10): 
    for key in dict.keys():
        if grade==key:
            value=dict[key]
            print(f"Your Grade is '{value['Letter_Grade']}' and {value['Performance']} Performance ") 
        else:
            continue 
else:
    print("Error!")
******************************************************************

# Question5

print("Question 5") 

n = 6

for i in range(n):
    # Printing spaces
    for j in range(i):
        print(' ', end='')
    # Printing alphabet
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='') 
    print() 
******************************************************************

#Question 6

print("Question 6")
condition=True

#Defining dictionary to store the values later 
mydict={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        SID=int(input("Enter the SID of Student- "))
        name=input("Enter the name of the Student- ")
        mydict[SID]=name
        prompt= input("If you want to store more students SID press Y/N- ")
        condition = True

    else:
        condition = False

print("Part a") 
for key,value in mydict.items():
    print(f"{key} is {value}")
print("")

print("Part b")
Name_sort_dict= sorted(mydict.values())
print(f"Name sorted dictionary is {Name_sort_dict}")
print("")

print("Part c")
SID_sort_dict= sorted(mydict.keys())
print(f"SID sorted dictionary is {SID_sort_dict}") 
print("")

print("Part D")
SID_find=int(input("Please enter the student's SID whose detail you want- "))
if SID_find in mydict.keys():
    print(f"Name of the student is {mydict[SID_find]}") 
else:
    print("The SID is not present in the given Data") 
print("")
*************************************************************

#Question 7

print("Question 7")
num=int(input("Total no. of terms of Fibonacci series that you want to print: ")) 

#Using the formula of the sum of previous two terms is equal to the present term.
a=0
b=1
n=0
#Initializing sum with first two terms 
sum=a+b

#Printing the initial two terms as the recursion is not valid on them
print(f"Fibonnaci sequence with {num} terms:")
print(a,end=" ")
print(b,end=" ") 

#Printing the remaining fibonnaci terms
while n<(num-2):
    a_n=a+b
    a=b
    b=a_n
    print(a_n,end=" ") 
    n=n+1
    sum += a_n 
# Finding average 
average=sum/num
# Printing average 
print(f"\nAverage of total {num} terms of sequence is {average}") 
print("") 
****************************************************************************

#Question 8

print("Question 8")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#Finding symmetric difference of both the sets
print("Part a")
set_notinboth=Set1^Set2
print(f"Set with elements not common in both is {set_notinboth}")


#Finding symmetric difference of all the three sets
print("Part b")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")


#Finding elements that are common in any two sets
print("Part C")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")


#Finding elements in set1 which range from 1 to 10
print("Part d")
new_set=set()
for n in range(1,11):
    new_set.add(n)
not_common_1=new_set- Set1
print(f"Set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")


#Finding elements in sets 1,2,3 and range from 1 to 10 
print("Part e")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"Set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}") 
   
