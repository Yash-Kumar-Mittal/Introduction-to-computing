
print("Question 1") 
#Defining the tower of Hanoi function
def tower_of_hanoi(n , source, destination, auxiliary): 
    step_number=1
    if n==1: 
        print (f"Move disk 1 from {source} to {destination}") 
        return
    tower_of_hanoi(n-1, source, auxiliary, destination) 
    print (f"Move disk {n} from {source} to {destination}")  
    tower_of_hanoi(n-1, auxiliary, destination, source) 
#Taking number of disk as input from the user
no_of_disk = int(input("Enter the number of disk in tower of Hanoi:\n")) 
print('''The Disks are numbered starting from top of the tower. 
Steps to move all the disks from Source Tower to Destination Tower is given below''')  
print()   
#Calling the function of tower of hanoi 
tower_of_hanoi(no_of_disk,"Source Tower","Destination","Auxiliary")




# Question 2
print("Question 2")
n = int(input("Enter the number of rows for Pascal's Triangle: "))
# Creating the pascal function and using recursion
print("Using recursions to create pascal's triangle: ")


def pascal(n, initial_n=n):
    if n == 0:
        return

    pascal(n-1, initial_n)
    print('  '*(initial_n-n), end='')
    a = 1
    for i in range(1, n+1):
        print(a, end='   ')
        a = a * (n - i) // i
    print()


pascal(n)

# Using loops to create pascal's triangle
print("Using loops to create pascal's triangle:")
for line in range(1, n+1):
    print('  '*(n - line), end='')
    b = 1
    for i in range(1, line+1):
        print(b, end='   ')
        b = b * (line - i) // i
    print()



print("Question 3") 
#Taking input from the user
n1=int(input("Enter first number:")) 
n2=int(input("Enter second number:"))
print() 
#Defining quotient and remainder function
def q_and_r_finder(x,y):
    quotient = (x // y)
    remainder = (x % y)
    return quotient,remainder
#Making a list of return values
list1=list(q_and_r_finder(n1,n2))
#a1=Quotient
q=list1[0]
#a2=Remainder
r=list1[1]
#Printing the quotient and remainder
print(f"The quotient when {n1} is divided by {n2} is {q}") 
print(f"The remainder when {n1} is divided by {n2} is {r}") 

#Que3.a 
print()
print("Que3.a")
c1=callable(q_and_r_finder)
c2=callable(n1)
c3=callable(n2)
if c1==True:
    print(f"Function is callable")
if c1==False:
    print(f"Function is Not-callable")
if c2==True:
    print(f"{n1} is callable")
if c2==False:
    print(f"{n1} is Not-callable")
if c3==True:
    print(f"{n2} is callable")
if c3==False:
    print(f"{n2} is Not-callable")
#Que3.b
print()
print("Que3.b") 
#list of values
listv=[q,r]
zero=False
if zero in listv:
    zero=True
else:
    zero=False
if zero==True:
    print("All result values are NOT 'non-zero'")  
elif zero==False:
    print("All result values are 'non-zero'")
#Que3.c
print()
print("Que3.c") 
#new values of list
listr=[q,r]
for i in range (4,7):
    listr.append(i)
listv2=[]
#adding number > 4 from listr to listv2
for i in listr:
    if i>4:
        listv2.append(i)
#a new list listv3 with same elements as listv2 but in string form
listv3=list(map(str,listv2))
#Using join
v=",".join(listv3)
print(f"Values greater than 4 are {v}")  
#Que3.d
print()
print("Que3.d") 
set1=set() 

#Adding above result in set datatype
for j in listv2:
    set1.add(j)
print("Above result in set form is shown below:")
print(set1)
#Que3.e
print()
print("Que3.e") 
#Making set1 immutable
frozenset(set1) 
print("The above set has been converted to immutable.") 
#Que3.f
print() 
print("Que3.f") 
print(f"Max value from set is {max(set1)}") 
#Using hash function
hash_value=hash(max(set1)) 
print(f"Hash value of {max(set1)} is {hash_value}")



print("Question4") 
#Forming a student named class 
class student:        
 #Using theconstructor to create class objects
    def __init__(self,name,roll_no):            
        self.name=name
        self.roll_no=roll_no
    #defing print function
    def getinfo(self): 
        print(f"Name of the student is {self.name} and roll no. is {self.roll_no}")  
    #Calling destructor
    def __del__(self):
        print("Destructor Called") 
#Making Yash an object of student
yash=student("Yash Kumar Mittal",21105069) 
yash.getinfo() 
del yash




print("Question5")
print() 
#Forming class Employee 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getinfo(self): 
        print(f"Employee Name is {self.name} and Salary is {self.salary}")

Mehak=Employee("Mehak",40000)
Ashok=Employee("Ashok",50000) 
Viren=Employee("Viren",60000) 
#Print Employee details
Mehak.getinfo()
Ashok.getinfo()
Viren.getinfo() 
#Updating the salary of Mehak to 70000
print("\nQue.5a")
Mehak.salary=70000
print("Mehak salary Updated to 70000")
Mehak.getinfo()
#Deleting the Viren's data 
print("\nQue.5b")
del Viren 
print("Employee Viren's data has been removed.")





print("Question 6") 

print("*******WELCOME TO THE FRIENDSHIP GAME*******")
print()   
#Defining the principle of Friendship Game
def anagram(word1,word2): 
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l1=[]
    l2=[]
    for i in word1:
        l1.append(i) 
    for j in word2: 
        l2.append(j)
    #Sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    else:
        return False

#Taking words as input by both the players 
George_word=str(input("Enter Word by George:")) 
Barbie_word=str(input("Enter Word by Barbie:")) 
#Using the anagram function
result=anagram(George_word,Barbie_word) 
#printing the final result
if result==True:
    print("\nFriendship of George and Barbie is REAL") 
elif result==False:
    print(f"\nFriendship of George and Barbie is FAKE")


