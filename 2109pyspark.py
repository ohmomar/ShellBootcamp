#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyspark
import findspark
findspark.init('/opt/anaconda3/lib/python3.11/site-packages/pyspark')
from pyspark import SparkContext
conf = pyspark.SparkConf().setMaster("local").setAppName("first")
sc = SparkContext(conf=conf)


# In[2]:


rdd=sc.parallelize([1,2,3])


# In[3]:


rdd.collect()


# In[4]:


sc


# In[5]:


rdd2 = sc.parallelize(["Python","SQL","Pyspark"])


# In[6]:


rdd2.collect()


# In[7]:


type(rdd2)


# In[8]:


rdd3 = sc.parallelize([1,2,3,4,5,6,7,8])


# In[9]:


rdd3.collect()


# In[10]:


rdd4=rdd3.map(lambda x:x*2)


# In[11]:


rdd4.collect()


# In[12]:


import findspark


# In[13]:


findspark.init()


# In[15]:


from pyspark.sql import SparkSession


# In[16]:


spark=SparkSession.builder.appName("RDDExample").getOrCreate()


# In[18]:


df=spark.createDataFrame([(1,2,3)])


# In[19]:


df.show()


# In[21]:


from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
df


# In[24]:


df.show()


# In[26]:


data2= [(1,'a','z',777700,'India'),(2,'b','y',9890,'India')]


# In[29]:


schema = "id int, name string,last_name string, mo int, country string"


# In[ ]:


shem_lisit()


# In[30]:


df3=spark.createDataFrame(data2,schema)


# In[31]:


df3.dtypes


# In[32]:


df3.show()


# In[33]:


users=[{"id":1,
        "first_name":"a",
        "amount_paid":1000
       },
       {"id":2,
        "first_name":"b",
        "amount_paid":1200
       }
      ]


# In[35]:


df4=spark.createDataFrame(users)


# In[36]:


df4.show()


# In[37]:


df5=spark.read.option("header",True).option("inferschema",True).csv("/home/labuser/ShellBootCamp2023/insurance.csv")


# In[39]:


df5.show()


# In[42]:


from pyspark.sql.functions import col


# In[41]:


df5.select("sex","region").show()


# In[44]:


df5.select(col("sex").alias("forename")).show()


# In[45]:


from pyspark.sql.functions import *


# In[50]:


df5.select(concat("sex",lit(" & "),"region")).show()


# In[51]:


df5.select("*",concat("sex",lit(" & "),"region")).show()


# In[52]:


df5.write.csv('/home/labuser/ShellBootCamp2023/finalemp')


# In[ ]:




