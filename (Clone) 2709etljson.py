# Databricks notebook source
print("Hello")

# COMMAND ----------

# #dbutils.fs.mount(
#  # source = "wasbs://raw@2709storageaccount.blob.core.windows.net",
#   #mount_point = "/mnt/2709storageaccount/raw",
#   extra_configs = {"fs.azure.account.key.2709storageaccount.blob.core.windows.net":"Qye9v5vgkFcZwhobROGZVqJ0vH6PRoxv+2YCgqwp/tAdD11wv+2UHyc6VAh04IhQ9VNtjysRyc6S+AStCsuv9Q=="})

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %fs ls dbfs:/mnt/2709storageaccount/raw

# COMMAND ----------

df=spark.read.json("dbfs:/mnt/2709storageaccount/raw/json/")

# COMMAND ----------

df.display()

# COMMAND ----------

 df1=df.withColumn("ingestiondate",current_timestamp()).withColumn("path",input_file_name())

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists json

# COMMAND ----------

df1.write.mode("overwrite").option("path","dbfs:/mnt/2709storageaccount/raw/json/ohm/json").saveAsTable("json.bronzetable")

# COMMAND ----------

df1.write.mode("overwrite")\
.option("path","dbfs:/mnt/2709storageaccount/raw/json/ohm/json_parquet")\
.format(parquet)\
.saveAsTable("json.bronzetabl_parquet")

# COMMAND ----------

# MAGIC %sql
# MAGIC select count(*) from json.bronzetable

# COMMAND ----------



# COMMAND ----------


