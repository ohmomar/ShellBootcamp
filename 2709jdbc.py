# Databricks notebook source
jdbcUsername = " "
jdbcPassword = " "
jdbcHostname = " "
jdbcPort = 1433
jdbcDatabase = " "
jdbcDriver= "com.microsoft.sqlserver.jdbc.SQLServerDriver"
jdbcUrl=f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};databaseName={jdbcDatabase};user={jdbcUsername};password={jdbcPassword}"

# COMMAND ----------

jdbcUsername = "nysql"
jdbcPassword = "Azure@7700"
jdbcHostname = "unextserver.database.windows.net"
jdbcPort = 1433
jdbcDatabase = "nydatabase"
jdbcDriver= "com.microsoft.sqlserver.jdbc.SQLServerDriver"

jdbcUrl=f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};databaseName={jdbcDatabase};user={jdbcUsername};password={jdbcPassword}"

# COMMAND ----------

df=spark.read.format("jdbc").option("url",jdbcUrl).option("dbtable", "SalesLT.Product").load()
display(df)

# COMMAND ----------


