#!/usr/bin/env python
# coding: utf-8

# In[2]:


def my_function(**product):
    print("The hardware product name is "+product["productname"])
my_function(productname="Mouse",brandname="Logitech")


# In[5]:


#Keyword only arguments
def nameAge(name,age):
    print("Hi, I am: ",name)
    print("My age is: ",age)
nameAge(name='Ohm',age=27)
nameAge(age=22,name='Ohm')


# In[6]:


#Positional only arguments
def nameAge(name,age):
    print("Hi, I am: ",name)
    print("My age is: ",age)
print("Case-1:")
nameAge('John',20)
print("Case-2:")
nameAge(20,'John')


# In[7]:


def minus(firstnum,secondnum):
    return firstnum-secondnum
a,b=20,10
result1=minus(a,b)
print(result1)
result2=minus(b,a)
print(result2)


# In[8]:


#using a class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj = Person('Ohm',22)
print(obj.name)
print(obj.age)


# In[9]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"

obj=Person('Ohm',22)
print(obj)


# In[11]:


class Person:
    def __init__(self,name,age):
        self.name= name
        self.age=age
    
    def myfunc(self):
        print("Hello my name is "+self.name+" and age is: "+str(self.age))
        
obj=Person('ohm',22)
obj.myfunc()


# In[13]:


class Person:
    def __init__(mysillyobject,name,age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is "+abc.name+" and age is: "+str(abc.age))
obj=Person('Ohm',22)
obj.myfunc()


# In[3]:


calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"
print(calc(21))


# In[4]:


filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums(): ",filter_nums("Geeks101"))

do_exclaim = lambda s:s + '!'
print("do_exclaim: ",do_exclaim("I am tired"))


# In[5]:


def cube(y):
    return y*y*y
lambda_cube = lambda num:num ** 3

print("invokving function with def keyword:")
print(cube(3))

print("invoking lambda function: ",lambda_cube(3))


# In[11]:


l = [1,2,9,-1]
print("Sorted numerically: ",sorted(l,key=lambda x: int(x)))
print("Filter positive even numbers: ",list(filter(lambda x:(x%2==0),l)))


# In[ ]:




