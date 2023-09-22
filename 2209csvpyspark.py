#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init()
from pyspark.sql import SparkSession
spark=SparkSession.builder.appName("csvexample").getOrCreate()


# In[31]:


from pyspark.sql.functions import *
from pyspark.sql.types import *


# In[2]:


input_files="/home/labuser/ShellBootCamp2023/"


# In[4]:


df_sales=spark.read.option("header",True).option("interschema",True).csv(f"{input_files}/transaction.csv")


# In[5]:


df_product=spark.read.option("header",True).option("interschema",True).csv(f"{input_files}/products.csv")


# In[6]:


df_sales.show()
df_product.show()


# In[8]:


df = df_sales.join(df_product, df_sales.product_id==df_product.product_id, "left")
df.show()


# In[10]:


df.filter("transaction_id=1").show()


# In[12]:


df.where("transaction_id<4").show()


# In[14]:


employees = [(1, "Scott", "Tiger", 1000.0, 
                      "united states", "+1 123 456 7890", "123 45 6789"
                     ),
                     (2, "Henry", "Ford", 1250.0, 
                      "India", "+91 234 567 8901", "456 78 9123"
                     ),
                     (3, "Nick", "Junior", 750.0, 
                      "united KINGDOM", "+44 111 111 1111", "222 33 4444"
                     ),
                     (4, "Bill", "Gomes", 1500.0, 
                      "AUSTRALIA", "+61 987 654 3210", "789 12 6118"
                     )
                ]


# In[15]:


employeesDF = spark. \
    createDataFrame(employees,
                    schema="""employee_id INT, first_name STRING, 
                    last_name STRING, salary FLOAT, nationality STRING,
                    phone_number STRING, ssn STRING"""
                   )


# In[16]:


employeesDF.show()


# In[28]:


from pyspark.sql import functions


# In[32]:


employeesDF.select(upper("nationality")).show()


# In[39]:


employeesDF.withColumn("nationality",upper("nationality")).withColumn("ssn_last4",substring(col("ssn"),-4,4).cast("int")).withColumn("country_code",split("phone_number"," ")[0].cast("int")).withColumn("area_code",split("phone_number"," ")[1].cast("int")).show()


# In[36]:





# In[35]:





# In[40]:


spark


# In[ ]:




