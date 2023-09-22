#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql.types import *


# In[2]:


import findspark
findspark.init()


# In[3]:


from pyspark.sql import SparkSession


# In[4]:


spark=SparkSession.builder.appName("2209example").getOrCreate()


# In[5]:


data=[(1,"a",30),(2,"b",32)]


# In[6]:


user_schema=StructType([StructField("id",IntegerType()),
                        StructField("name",StringType()),
                        StructField("age",IntegerType())
                       ])
df=spark.createDataFrame(data,user_schema)


# In[7]:


df.show()


# In[8]:


data=[
    (1,"Alice",["Reading","Hiking"]),
    (2,"Bob",["Swimming","Gardening","Painting"]),
    (3,"Charlie",["Cooking"]),
    (4,"David",["Photography","Skiing","Cooking"])
]


# In[9]:


user_schema2=StructType([StructField("id",IntegerType()),
                         StructField("name",StringType()),
                         StructField("hobby",ArrayType(StringType()))
                        ])


# In[11]:


df2=spark.createDataFrame(data,user_schema2)


# In[13]:


df2.show()


# In[14]:


from pyspark.sql.functions import *


# In[23]:


df2.select("id","name",explode("hobby").alias("hobby")).show()


# In[29]:


df3=df2.withColumn("hobby",explode("hobby")).withColumn("ingestion_data",current_timestamp())


# In[30]:


df3.show(truncate=False)


# In[ ]:




