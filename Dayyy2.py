#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a program to create a function that takes two arguments, name and age, and print their value.
def f(name, age):
    print(name, age)
    
a = f("ABC", 23)


# In[5]:


#Write a program to create function func1() to accept a variable length of arguments and print their value.
def funct1(*num):
    for i in num:
        print(i)
print("Value")
funct1(12,89,23)
print("\nAnother value")
funct1(23, 12)  


# In[7]:


#Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.
def cal(v1, v2):
    sum1 = v1 + v2
    sub = v1 - v2
    return sum1, sub

a = cal(20, 5)
print(a)


# In[8]:


#Create a function with a default argument
def func(name, salary = 9000):
    print("Name", name, "Salary:", salary)

func("Abc", 10000)
func("xyz")


# In[9]:


#Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.
def rec(num):
    if num:
        return num + rec(num-1)
    else:
        return 0
    
a = rec(10)
print(a)


# In[12]:


#Assign a different name to function and call it through the new name
def student(name, age):
    print(name, age)
    
student("A", 12)

show_student= student
show_student("B", 22)


# In[13]:


#Generate a Python list of all the even numbers between 4 to 30
print(list(range(4,30,2)))


# In[14]:


#Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]
y = max(x)
print(y)


# ## String

# In[15]:


#Write a program to create a new string made of an input string’s first, middle, and last character.
s1 = "Patel"
print("Original string is: ", s1)

l = s1[0]
l2 = len(s1)
m = int(l2/2)

l = l + s1[m]
l = l + s1[l2-1]
print(l)


# In[19]:


#Create a string made of the middle three characters
def middle(str1):
    print("Original string: ", str1)
    
    a = int(len(str1)/2)
    b = str1[a-1:a+2]
    print("Middle 3 char. are: ", b)
    
middle("abcdefg")  
middle("aeiou")


# In[23]:


#Append new string in the middle of a given string
def middle1(s1, s2):
    print("strings: ", s1, s2)
    
    m1 = int(len(s1)/2)
    a = s1[:m1:]
    a = a + s2
    a = a + s1[m1:]
    print("Appending new string in middle: ", a)
    
middle1("School", "name")
    


# In[24]:


#Create a new string made of the first, middle, and last characters of each input string
def mix(s1, s2):
    fc = s1[0] + s2[0]
    mc = s1[int(len(s1)/2):int(len(s1)/2) + 1] + s2[int(len(s2)/2): int(len(s2)/2)+1]
    lc = s1[len(s1)-1] + s2[len(s2)-1]
    
    total = fc + mc + lc
    print("Mix string is: ", total)
mix("Hello", "GoodMorning")


# In[28]:


#Count all letters, digits, and special symbols from a given string
def func(str1):
    char1 = 0
    digit = 0
    symbol = 0
    
    for i in str1:
        if i.isalpha():
            char1 += 1
        elif i.isdigit():
            digit += 1
        else:
            symbol += 1
            
    print("Charecters=", char1, "Digits=", digit, "Symbol=", symbol)
    
a = "Ajo46!j9dg%jd3#"
print("Counts -")
func(a)


# In[30]:


#Create a mixed String using the following rules
#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
s1 = "zyx"
s2 = "cab"

s1_l = len(s1)
s2_l = len(s2)

length = s1_l if s1_l > s2_l else s2_l
r = ""

s2 = s2[::-1]

for i in range(length):
    if i < s1_l:
        r = r + s1[i]
        
    if i < s2_l:
        r = r + s2[i]
print(r)        


# In[34]:


#Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
def bal(s1, s2):
    a = True
    for i in s1:
        if i in s2:
            continue 
        else:
            a = False
    return a

s1 = "ab"
s2 = "abc circle"
a = bal(s1,s2)
print("Result:",a)


# In[38]:


#Write a program to find all occurrences of “USA” in a given string ignoring the case.
str1 = "Welcome to USA. usa awesome, isn't it?"
str2 = "USA"

s = str1.lower()
c1 = s.count(str2.lower())
print("USA count:", c1)



# In[39]:


#Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
str1 = "PYnative29@#8496"
total = 0
cnt = 0
for i in str1:
    if i.isdigit():
        total += int(i)
        cnt += 1
avg = total/cnt
print("Sum is:", total, "Average is", avg)


# In[42]:


#Write a program to count occurrences of all characters within a string
str1 = "Banana"
dict1 = dict()
for i in str1:
    a = str1.count(i)
    dict1[i] = a
print("Result:", dict1)
    


# In[46]:


#Reverse a given string
a= "PYnative"
a = a[::-1]
print("Reverse string: ", a)


# In[48]:


#Write a program to find the last position of a substring “Emma” in a given string.
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("String is:", str1)

a = str1.rfind("Emma")
print("last occurrence of Emma at index:", a)


# In[50]:


#Write a program to split a given string on hyphens and display each substring.
str1 = "Emma-is-a-data-scientist"
print("String is:", str1)
subs = str1.split("-")
print("Sub-string is:")

for i in subs:
    print(i)


# In[52]:


#Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
r_list=[]

for i in str_list:
    if i:
        r_list.append(i)
print(r_list)        


# In[54]:


#Remove special symbols / punctuation from a string
import string
str1 = "/*Jon is @developer & musician"
print("String is:", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))
print("Result is:", new_str)


# In[55]:


#Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
print("String is:", str1)

a = "". join([i for i in str1 if str1.isdigit()])
print(a)


# In[58]:


#Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"
print("String is:", str1)

a = []
temp = str1.split()

for item in temp:
    if any(i.isalpha() for i in item) and any(i.isdigit() for i in item):
        a.append(item)

print("Words with alpha. and numbers:")
for j in a:
    print(j)
    


# In[62]:


#Replace each special symbol with # in the following string
import string
str1 = '/*Jon is @developer & musician!!'
print("String is:", str1)
rp = "#"

for i in string.punctuation:
    str1 = str1.replace(i, rp)
print("Result:", str1)    


# ## Python Data Structure Exercise

# In[65]:


#Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
r = list()

odd = l1[1::2]
print("Odd element position:", odd)

even = l2[0::2]
print("Even element position:", even)

print("Final list:")
r.extend(odd)
r.extend(even)
print(r)


# In[66]:


#Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
list1 = [34, 54, 67, 89, 11, 43, 94]
print("List is:", list1)

el = list1.pop(4)
print("After removing 4th element: ", list1)

list1.insert(2,el)
print("Ater adding element at 2nd position:", list1)

list1.append(el)
print("Final list:", list1)
      


# In[ ]:


#Slice list into 3 equal chunks and reverse each chunk
list1 = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("List is:", list1)

size = int(len(list1)/3)
start = 0
end = size

for i in range(3):
    ins = slice(start, end)
    
    chunk = list1[]


# In[68]:


#Count the occurrence of each element from a list
list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]
a = dict()

for i in list1:
    if i in a:
        a[i] += 1
        
    else:
        a[i] = 1

print(a)


# In[69]:


#Create a Python set such that it shows the element from both lists in a pair
list1 = [2, 3, 4, 5, 6, 7, 8]
list2= [4, 9, 16, 25, 36, 49, 64]

r = zip(list1, list2)
rset = set(r)
print(rset)


# In[72]:


#find the intersection (common) of two sets and remove those elements from the first set
s1 = {23, 42, 65, 57, 78, 83, 29}
s2 = {57, 83, 29, 67, 73, 43, 48}

a = s1.intersection(s2)
print("Interaction is:", a)

for i in a:
    s1.remove(i)
print(s1)


# In[74]:


#Checks if one set is a subset or superset of another set. If found, delete all elements from that set
s1 = {27, 43, 34}
s2 = {34, 93, 22, 27, 43, 53, 48}

print("first set is subset of secound:", s1.issubset(s2))
print("secound set is subset of first:", s2.issubset(s1))

print("first set is super-set of secound:", s1.issuperset(s2))
print("secound set is super-set of first:", s2.issuperset(s1))


if s1.issubset(s2):
    s1.clear()
if s2.issubset(s1):
    s2.clear()
    
print("first set:", s1)
print("secound set:", s2)


# In[75]:


#Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

roll_number[:] = [i for i in roll_number if i in sample_dict.values()]
print(roll_number)


# In[82]:


#Remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print("Main list:", sample_list)
l1 = list(set(sample_list))
print("Unique list:", l1)

l2 = tuple(l1)
print("Tuple:",l2)
print("Min:", min(l2))
print("Max:", max(l2))


# ## Python List Exercise

# In[89]:


#Reverse a list in Python
list1 = [100, 200, 300, 400, 500]
print(list1)
list1.reverse()
print(list1)


# In[90]:


#concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

a = [i + j for i, j in zip(list1, list2)]
print(a)


# In[91]:


#Turn every item of a list into its square
n = [1, 2, 3, 4, 5, 6, 7]
a = []

for i in n:
    a.append(i*i)
print(a)
    


# In[93]:


#Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
r = [a+b for a in list1 for b in list2]
print(r)


# In[95]:


#Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for a,b in zip(list1, list2[::-1]):
    print(a,b)


# In[96]:


#Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
r = list(filter(None, list1))
print(r)


# In[97]:


#Write a program to add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)
print(list1)


# In[99]:


#Extend nested list by adding the sublist
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)
print(list1)


# In[102]:


#Replace list’s item with new value if found
#Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.
list1 = [5, 10, 15, 20, 25, 50, 20]
i1 = list1.index(20)
list1[i1] = 200
print(list1)


# In[104]:


#Remove all occurrences of a specific item from a list.
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
    
print(list1)


# In[ ]:




