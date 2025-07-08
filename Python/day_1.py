print("Hello World")
print("Welcome to the python world!")

#This is comment so you can avoid it.

#Also this is single line comment.

#python version

import sys
print(sys.version)

#python indentation 
if 5>2:
    print("Five is greater than two!")


if 2>2:
    print("Five is greater than two!")
else:
    print("I'm From else portion broo!")

#variables
x=5
y="Hello Tareq"
#in print if i use , print n blank space 

print("This is a testing","part for blank space")# This is also a comment

print(y,"\n",x)

#here is an problem if string print first and number last number having an blank space 


# This
# is 
# a multiple 
# line
# comment


"""This
is 
also
a multiple 
line
comment"""

"""
Hello Broo
I'm a good
exaple for 
multiple line 
comment 
"""

#pyhon has no command for declaring a variable

print(y)
print(x)

a=10000
b=1.3493
c="hey this is variation of the number"
d='iam char'
e='A'
print(a)
print(b)
print(c)
print(d)
print(e)

#print the number is which type
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# python only have string not char

"""Now we learn about casting"""
p=9
q="3"
r=7.0
print(p,q,r)
print(type(p),type(q),type(r))

#casting
m=str(p)
n=float(p)
print(m,n,r)
print(type(m),type(n),type(r))

m=int(q)
n=float(q)
print(m,n,r)
print(type(m),type(n),type(r))

m=int(r)
n=str(r)
print(m,n,r)
print(type(m),type(n),type(r))

s="Tareq"
#is the same as
s='Tareqs'
#here is  override the variable

print(s,s)

"""Python also a case sensetive language"""

a=10000
A="Tareq"
#A will not overwrite with a 
print(a, A)

"""Variable name same as another"""
#camelCase thisIsCamelCaseVariable

#PascalCase ThisIsPascalCase

#snake_casse this_is_snake_case_variable

"""python variables assign multiple values"""

m,n,o,p,q="Tareq","Asif","Jahangir","Fuad","Moksud"
print(m)
print(n)
print(o)
print(p)
print(q)

m=n=o=p=q="This is Tareq"

print(m)
print(n)
print(o)
print(p)
print(q)

"""Unpacking collection"""
fruits=["Mango", "Banana", "Lemon", "Jackfruits", "Orange"]
"""Collection e joto ta item thak be toto ta valriable create kore unpack korte hobe"""
m,n,o,p,q=fruits

print(m)
print(n)
print(o)
print(p)
print(q)
print(fruits)
m=fruits
print(m)
m,n,x,y,z=fruits
print("I am from unpack portion")
print(m)
print(n)
"""Global variable"""

x="awasome"

def myfunc():
    print("Tareq is "+x)

myfunc()

def myfunc():
    x="fentastic" #this is local variavle
    print("Tareq is "+x)

myfunc()

print("Tareq is also "+x)

def myfunc():
    global x 
    x="fantastic"
    print("Tareq is "+x)

myfunc()

print("Tareq is also "+x)

x="Awesome"

def myfunc():
    global x
    x="Fantastic"
    print("This is a from function "+x)

myfunc()

print("Pytohn is "+x)