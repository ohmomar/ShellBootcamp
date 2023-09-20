#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input("Enter number1: "))
b=int(input("Enter number2: "))
print("Sum of a&b is :",a+b)
print("Difference of a&b is :",a-b)


# In[7]:


print(f"Sum of {a} and {b} is",a+b)


# In[9]:


#min age for voting
age = int(input("Enter the age: "))

if age>=18:
    print("Eligible to vote")
else:
    print(f"You are {18-age} years left to vote")


# In[12]:


#raw string
print("C:/programfiles/backup/newfolder/abcd/xyz")
print(r"C:\programfiles\backup\newfolder\tbcd\xyz")


# In[29]:


#sets
s={1,2,3,4,5,6,7,8,9,10,9,8,11,25,15}
s.add(40)
s.add(30)
s


# In[30]:


print(s)


# In[31]:


s.discard(7)
s


# In[32]:


s.remove(10)


# In[34]:


s.pop()
s


# In[35]:


a={1,2,3,4,5}
s|a


# In[36]:


s&a


# In[37]:


s-a #difference  set1-(set1&set2)


# In[38]:


s^a #symmetric difference (union of uncommon elements)


# In[45]:


#dictionar
d1={4:"c",2:"Java",8:"Python"}
d1[2]


# In[46]:


d1.get(8)


# In[48]:


d1.get(1,"Key not found")


# In[49]:


get_ipython().run_cell_magic('writefile', 'p1.py', 'class Student:\n    #Constructor\n    def __init__(self, name, rollno, section, email, stream):\n        self.name = name\n        self.rollno = rollno\n        self.section = section\n        self.email = email\n        self.stream = stream\n        \n    #Add student\n    def add_student(self, nname, rrollno, ssection, eemail, sstream):\n        ob=Student(nname, rrollno,ssection,eemail,sstream)\n        lst.append(ob)\n        \n    #Display students\n    def disp_student(self,ob):\n        print("Name: ",ob.name)\n        print("Roll Number: ",ob.rollno)\n        print("Section: ",ob.section)\n        print("Email: ",ob.email)\n        print("Stream: ",ob.stream)\n        print("\\n")\n        \n    #Function to search the student\n    def search_student(self,rname):\n        k=0\n        for i in range(lst.__len__()):\n            if(lst[i].name==rname):\n                print(lst[i].name)\n                return i\n            else:\n                return k\n            \n    #Delete the student        \n    def delete_student(self,rname):\n        i=obj.search_student(rname)\n        if i==-2:\n            print("Student Not Found!!")\n        else:\n            del lst[i]\n    \n    #Update Student Name\n    def update_student(self,rrname,ssname):\n        i=obj.search_student(rrname)\n        if i==-2:\n            print("Student Not Found!!")\n        else:\n            rrname=ssname\n            lst[i].name=rrname\n        \nlst=[]\nobj=Student(\'\',0,\'\',\'\',\'\')\nprint("1. Add a new student")\nprint("2. Display all students")\nprint("3. Search a student")\nprint("4. Delete a student")\nprint("5. Update a student name")\nprint("To exit enter any number")\n\nwhile(1):\n    inputd = int(input("Enter Your Choice: "))\n    if inputd == 1:\n        print("ENTER NEW STUDENT DETAILS")\n        nname = input("Student Name: ")\n        nrollno = input("Student Roll Number: ")\n        nsec = input("Student Section: ")\n        nemail = input("Student Email: ")\n        nstream = input("Student Stream: ")\n        obj.add_student(nname,nrollno,nsec,nemail,nstream)\n    elif inputd == 2:\n        print("LIST OF STUDENTS")\n        for i in range(lst.__len__()):\n            obj.disp_student(lst[i])\n    elif inputd == 3:\n        print("SEARCH STUDENT")\n        sename = input("Enter student name to search:")\n        ans = obj.search_student(sename)\n        if ans!=-2:\n            print("Student Found!!")\n        else:\n            print("Student Not Found!!")\n    elif inputd == 4:\n        print("DELETE STUDENT")\n        delname = input("Enter student name to delete: ")\n        obj.delete_student(delname)\n    elif inputd == 5:\n        print("UPDATE STUDENT")\n        oldname = input("Enter student name to be updated: ")\n        newname = input("Enter updated name of the student: ")\n        obj.update_student(oldname,newname)\n')


# In[50]:


get_ipython().run_cell_magic('writefile', 'abc.cpp', '#include<iostream.h>\nusing namespace std;\nint main()\n{\n    cout<<"Hello! Ohm";\n    return 0;\n}\n')


# In[51]:


lst1 = ['p1','p2','p3','p4']
lst2 = ['pizza','burger','pasta','french fries']
d2 = dict(zip(lst1,lst2))
d2


# In[52]:


#numpy
import numpy as np
a=np.array(12)
a


# In[53]:


a=np.array(1,2,3,4,5,6,7)
a


# In[54]:


a.ndim


# In[55]:


a=np.array([1,2,3,4,5])
a.ndim


# In[56]:


a


# In[57]:


a.shape


# In[58]:


a.size


# In[59]:


a.dtype


# In[60]:


a=np.array([1.9,2,3,4,5])
a.dtype


# In[61]:


a=np.array([1.9,2,3,4,5,'a'])
a.dtype


# In[64]:


a=np.array(['aaa','ab','bb'])
a.dtype


# In[65]:


import matplotlib.pyplot as plt
import numpy as np


# In[70]:


a=np.array([[[270,270,270]]])
plt.imshow(a)


# In[72]:


x=np.arange(0,10,0.1)
x


# In[78]:


y=np.sin(x)
plt.plot(x,y,color='black',linewidth=4,linestyle='dotted')
plt.fill_between(x,y,color='blue',alpha=0.9)
plt.show()


# In[84]:


x=['A','B','C','D']
y=[10,20,50,30]
colors12=['r','g','b','c']
plt.bar(x,y,color=colors12)
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.xticks(rotation=90)
plt.yticks(rotation=45)
plt.show


# In[86]:


hours=[6,12,2,4]
chores=["sleep","work","food","leisure"]
cols1=["red","green","blue","cyan"]
plt.pie(hours,labels=chores,colors=cols1,counterclock=False,autopct='%1.2f%%',explode=[0,0,0.3,0])
plt.legend()
plt.show


# In[87]:


import pandas as pd


# In[88]:


#series - 1 dimensional
#dataframe - 2 dimensional


# In[95]:


s1=[100,200,300,400,500,600,700]
#s1=np.array([100,200,300,400,500,600,700])
sr1=pd.Series(s1)
sr1


# In[96]:


type(sr1)


# In[97]:


d = {'col1':[100,200,300,400,500],'col2':[200,300,400,500,600]}
d


# In[99]:


s2=pd.Series(d)
s2


# In[100]:


df1=pd.DataFrame(d)
df1


# In[124]:


df = pd.read_csv('/home/labuser/Downloads/insurance.csv')
df


# In[105]:


df.shape


# In[106]:


df.size


# In[107]:


df.info()


# In[111]:


df.describe(include='all').T


# In[112]:


df.isnull().sum()


# In[116]:


#extract a column and create a series
#df['age']
#df.age

#extract a column and create a dataframe
#df.iloc[:,0:1]
#df.iloc[:,:]
df.iloc[:,[0]]


# In[119]:


df.iloc[:,[2,5,6]]


# In[120]:


df.iloc[30:42,:]


# In[121]:


df.iloc[[100,200,300,400],:]


# In[122]:


df.drop(columns='smoker',axis=1, inplace = True)#delete column in orignal data (use inplace = True)


# In[123]:


df


# In[127]:


x=df.drop(columns='smoker',axis=1)
x


# In[128]:


df['region'].unique()


# In[129]:


df['region'].nunique()


# In[130]:


df['region'].value_counts()


# In[132]:


df['region'].value_counts().plot(kind='pie')


# In[133]:


df['region'].value_counts().plot(kind='line')


# In[135]:


df.head() #top 5 rows


# In[136]:


df.tail(10)#last 10 values


# In[138]:


df.select_dtypes(include=['int64','float64'])


# In[139]:


plt.plot(df.age,df.charges)


# In[140]:


plt.bar(df.age,df.charges)


# In[141]:


plt.scatter(df.age,df.charges)


# In[142]:


plt.hist(df.charges)


# In[143]:


plt.boxplot(df.charges)


# In[145]:


#filtering of data
df[df.region == "southwest"]


# In[152]:


df[(df.region == "southwest")&(df.smoker=='no')]


# In[156]:


df[(df.region == "southwest")&(df.smoker=='yes')&(df.sex=='female')]


# In[159]:


df.smoker=df.smoker.replace(to_replace=["yes","no"],value=[1,0])
df.smoker


# In[160]:


len(df[(df.region == "southwest")&(df.smoker==0)&(df.sex=='female')])


# In[161]:


df.sort_values(by='region')


# In[ ]:




