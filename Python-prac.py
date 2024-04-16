#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

n1 = 20
n2 = 40

if n1 * n2 <= 1000:
    print(n1 * n2)
else:
    print(n1 + n2)
       


# In[6]:


def numbers(n1, n2):
    a = n1 * n2
    
    if a <=1000:
        return a
    else:
        return n1 + n2
    
b = numbers(50, 70)
print(b)

c = numbers(10, 20)
print(c)


# In[8]:


#Print the sum of the current number and the previous number
prev_num = 0

for i in range(1,11):
    sum = prev_num + i
    print("Sum of current number", i, "previous number", prev_num,"is:", sum)
    prev_num = i
    


# In[10]:


#Print characters from a string that are present at an even index number

a = "PythonWorld"
for i in range(0, len(a), 2):
    print(a[i])


# In[11]:


#Remove first n characters from a string
def remove(string, n):
    print("String name: ", string)
    a = string[n:]
    return a

s1 = remove("Hello", 2)
s2 = remove("India", 3)

print(s1)
print(s2)


# In[15]:


#Check if the first and last number of a list is the same
def check(num):
    print("List:", num)
    
    firstIndex = num[0]
    lastIndex = num[-1]
    
    if firstIndex == lastIndex:
        return True
    else:
        return False
    
n1 = check([1,2,3,4,5,6])
print(n1)

n2 = check([32,45,67,23,32])
print(n2)


# In[16]:


#Display numbers divisible by 5 from a list
listnum = [20, 25, 67, 35, 53, 60]
print("Listy is: ", listnum)

for i in listnum:
    if i%5 == 0:
        print(i)
    


# In[18]:


#Return the count of a given substring from a string
a = "Hello Sir, Hello Madam"
b = a.count("Hello")
print(b)


# In[21]:


#print pattern 
for i in range(6):
    for j in range(i):
        print(i, end=" ")
    print("\n")


# In[27]:


#Check Palindrome Number
def palingdrom(num):
    number = str(num)
    return number == number[::-1]

n1=212
if palingdrom(n1):
    print(f"{n1} is a palingdrome")
    
else:
    print(f"{n1} is not palingdrome")


# In[28]:


#Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
def twolist(l1, l2):
    finalList = []
    
    for i in l1:
        if i % 2 != 0:
            finalList.append(i)
            
    for i in l2:
        if i % 2 == 0:
            finalList.append(i)
            
    return finalList

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
print("Result list is:", twolist(l1,l2))


# In[30]:


#Write a Program to extract each digit from an integer in the reverse order.
num = 34981
print("Number :", num)
while num > 0:
    a= num % 10
    num = num // 10
    print(a, end="")


# In[31]:


#Calculate income tax for the given income by adhering to the rules below
#10000*0% + 10000*10%  + 25000*20% = $6000.

salary = 50000
tax = 0

if salary <= 10000:
    tax = 0
    
elif salary <= 20000:
    a = salary - 10000
    tax = a * 0.1
    
else:
    tax = 10000 * 0.1 + (salary - 20000) * 0.20
    
print("Total tax is: ", tax)



# In[38]:


#print multiplication table from 1 to 10
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end=" ")
    print("\t\t")    


# In[43]:


#Print a downward Half-Pyramid Pattern of Star
for i in range(7, 0, -1):
    for j in range(0, i-1):
        print('*', end=" ")
    print( " ")


# In[45]:


#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    return base ** exp

op = exponent(2,6)
print(op)


# ## Python Input and Output Exercise

# In[46]:


#Write a program to accept two numbers from the user and calculate multiplication
a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))

m = a1 * a2
print("Multiplication of two numbers is: ", m)


# In[47]:


#Display three string “Name”, “Is”, “James” as “Name**Is**James”
print("Name", "Is", "James", sep='**')


# In[55]:


#Convert Decimal number to octal using print() output formatting
number = 45
print('%o' % number)


# In[58]:


#Display float number with 2 decimal places using
a = 456.7654
print('%.2f'% a)


# In[60]:


#Accept a list of 5 float numbers as an input from the user
l = []
for i in range(0,5):
    print("Enter index number", i , "-")
    f = float(input())
    l.append(f)
print("Input list is- ", l)


# In[68]:


#accept any three string from one input() call
a1, a2, a3 = input("Enter name: ").split()
print("First name: ", a1)
print("Secound name: ", a2)
print("Third name: ", a3)


# In[70]:


#Format variables using a string.format() method.
quantity = 3
totalMoney = 1000
price = 450
a=("I have {1} dollars so I can buy {0} football for {2:.2f} dollars.")
print(a.format(quantity, totalMoney, price))


# ## Python if else, for loop, and range()
# 

# In[1]:


i = 1
while i <= 10:
    print(i)
    i += 1


# In[3]:


#Print the following pattern
a = 5
for i in range(1, a+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print(" ")
              


# In[5]:


#Calculate the sum of all numbers from 1 to a given number
sum = 0
a = int(input("Enter number: "))

for i in range(1, a+1):
    sum += i
print("sum is: ", sum)


# In[7]:


#Write a program to print multiplication table of a given number
number = 5
for i in range(1,11):
    p = number * i
    print(number, "X", i, "=", p)


# In[8]:


#Display numbers from a list using loop
#Write a program to display only those numbers from a list that satisfy the following conditions

#The number must be divisible by five
#If the number is greater than 150, then skip it and move to the next number
#If the number is greater than 500, then stop the loop

l = [12, 67, 50, 150, 32, 135, 90, 180]

for i in l:
    if i>500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)


# In[11]:


#Count the total number of digits in a number
def countnum(num):
    return len(str(num))

a = countnum(123456)
print("Total number of digits is:",a)


# In[12]:


#Write a program to use for loop to print the following reverse number pattern
a = 5
b = 5
for i in range(0, a+1):
    for j in range(b-i, 0, -1):
        print(j, end=" ")
    print()


# In[13]:


#Print list in reverse order using a loop
list1 = [34, 65, 12, 98, 45, 22]
list2 = reversed(list1)
for item in list2:
    print(item)


# In[16]:


#Display numbers from -10 to -1 using for loop
for i in range(-10, 0, 1):
    print(i)


# In[18]:


#Use else block to display a message “Done” after successful execution of for loop
for i in range(0,7):
    print(i)
else:
    print("Done")


# In[36]:


#Write a program to display all prime numbers within a range
start = 25
end = 30

for i in range(start, end + 1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break          
        else:
            print(i)


# In[44]:


#Display Fibonacci series up to 10 terms
n1 = 0
n2 = 1

for i in range(10):
    print(n1, end=" ")
    r = n1 + n2
    
    n1 = n2
    n2 = r


# In[56]:


#Find the factorial of a given number
def fac(n):
    if n==1:
        return 1
    else:
        return n * fac(n-1)
    
a = fac(5)
print(f"Factorial is: ", a)


# In[59]:


#Use a loop to display elements from a given list present at odd index positions
l = [1, 4, 6, 3, 7, 9, 12, 54, 76, 87, 34, 22]
for i in l[1::2]:
    print(i)


# In[60]:


#Calculate the cube of all numbers from 1 to a given number
number = 5
for i in range(1, number+1):
    print("Cube of number ", i, "is", (i*i*i))

