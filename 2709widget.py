# Databricks notebook source
dbutils.help()

# COMMAND ----------

dbutils.widgets.help()

# COMMAND ----------

dbutils.widgets.combobox(name="database",defaultValue="default",choices=["default","json","sample","test"],label="databases")

# COMMAND ----------

dbutils.widgets.get("database")

# COMMAND ----------

dbutils.widgets.remove("database")

# COMMAND ----------


