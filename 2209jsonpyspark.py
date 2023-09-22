#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("JsonExample").getOrCreate()


# In[6]:


from pyspark.sql.functions import *


# In[ ]:


from 


# In[2]:


input_files="/home/labuser/ShellBootCamp2023/"


# In[3]:


df=spark.read.json(f"{input_files}/constructors.json")


# In[5]:


df.show(truncate=False)


# In[7]:


df_final=df.withColumn("ingestion_date",current_timestamp()).withColumn("path",input_file_name()).drop("url")


# In[8]:


df_final.show()


# In[13]:


df_final=df_final.drop("path")


# In[10]:


output_files="/home/labuser/ShellBootCamp2023/processed_data/constructor_parquet"


# In[14]:


df_final.write.parquet(f"{output_files}")


# In[15]:


df_final.write.mode("overwrite").parquet(f"{output_files}")


# In[16]:


df_final.write.mode("overwrite").saveAsTable("constructor")


# In[18]:


spark.sql("select * from constructor").show()


# In[19]:


spark.sql("select * from constructor where constructorId=10").show()


# In[20]:


df_final.write.mode("overwrite").option("path","/home/labuser/ShellBootCamp2023/processed_data/construct_table").saveAsTable("constructor")


# In[23]:


df_ps=spark.read.option("multiline","true").json("/home/labuser/ShellBootCamp2023/pitstop.json")


# In[24]:


df_ps.show()


# In[26]:


df_ps.drop_duplicates().sort("driverId").show()


# In[45]:


df_final=df_ps.sort("driverId")


# In[47]:


df_ps.count()


# In[30]:


df_pstemp=df_ps.groupby("stop").count()


# In[31]:


import matplotlib.pyplot as plt


# In[35]:


df_pandas = df_pstemp.toPandas()


# In[36]:


plt.bar(df_pandas["stop"],df_pandas["count"])


# In[41]:


df_final.show()


# In[48]:


df_final.write.mode("overwrite").option("path","/home/labuser/ShellBootCamp2023/processed_data/pitstops").saveAsTable("SortedConstructor")


# In[49]:


spark.sql("select * from SortedConstructor").show()


# In[ ]:




