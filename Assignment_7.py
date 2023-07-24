#!/usr/bin/env python
# coding: utf-8

# Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
# and store the results in variables. Then print the data in the following format by calling the
# variables:
# First variable is __ & second variable is __.
# Addition: __ + __ = __
# Subtraction: __ - __ = __
# Multiplication: __ * __ = __
# Division: __ / __ = __

# In[12]:


a = int(input("Enter the first number a:"))
b = int(input("Enter the second variable b:"))
add= a+b
sub= a-b
mul= a*b
div= a/b
print(f"First Variable is {a} & Second Variable is {b} .")
print(f"Addition: {a} + {b} = {add}")
print(f"Subtraction:{a} - {b} = {sub}")
print(f"Multiplication:{a} * {b} = {mul}")
print(f"Division:{a} / {b} = {div}")


# Q.2. What is the difference between the following operators:
# (i) ‘/’ & ‘//’
# (ii) ‘**’ & ‘^’
(i) / = This displays the quotient value with decimal value of the divison
   // = This displays the quotient value without decimal
# In[11]:


a=6
b=2
c=a/b
d=a//b
print(f"{a} / {b} = {c}")
print(f"{a} // {b} = {d}")

(ii) ** = It is the power operator . a**b in this it displays the power of a with b
     ^ = XOR operator.It converts the given number to decimal value and Sets each bit to 1 if only one of two bits is 1. 
         The decimal value willl covert to the number.
# In[10]:


a=6
b=2
c=a**b
d=a^b
print(f"{a} ** {b} = {c}")
print(f"{a} ^ {b} = {d}")


# Q.3. List the logical operators.
and, or , not 
# Q.4. Explain right shift operator and left shift operator with examples.
Left shift operator:
    this operator is used to add the zeros to the right of the decimal no.
    
example:
    Here the given value is 10 -- decimal value: 1010
    When the left shift is given the zeros are shifted to right of the decimal number and it becomes- 101000
    the value of 1010100 - 40
    
# In[18]:


i=10
x=i<<2
print(x)

In right shift it removes the number of digits given from the last.

Example:
    In the below example the right shift to 2.
    THe given number is 10 - 1010
    the right shift means removing two digits from the last means 0010
    the value of 0010 is 2
# In[19]:


i=10
x=i>>2
print(x)


# Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is
# present in the list or not.

# In[17]:


len1=15
l1=[]
for i in range(len1):
    a=int(input(f"Enter the number {i}:"))
    l1.append(a)
print(l1)
for i in range(len1):
    if i == 10:
        print("10 is present in list")

