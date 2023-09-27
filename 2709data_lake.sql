-- Databricks notebook source
create schema sample

-- COMMAND ----------

create table employee(id int, name string, age int, dept string) location "dbfs:/mnt/2709storageaccount/raw/delta/naval/emp"

-- COMMAND ----------

describe extended employee

-- COMMAND ----------

describe history employee

-- COMMAND ----------

select * from employee

-- COMMAND ----------

insert into table employee values(1,'a',23,'DE')

-- COMMAND ----------

select * from employee

-- COMMAND ----------

describe history employee

-- COMMAND ----------

insert into table employee values(2,'b',23,'DE')

-- COMMAND ----------

insert into table employee values(3,'c',23,'DE'),
                            (4,'d',23,'DE')

-- COMMAND ----------

describe history employee

-- COMMAND ----------

select * from employee

-- COMMAND ----------

delete from employee where id= 1

-- COMMAND ----------

select * from employee

-- COMMAND ----------

Update employee
set dept='DS'
where id= 4

-- COMMAND ----------

describe history employee

-- COMMAND ----------

select * from employee

-- COMMAND ----------

select * from employee version as of 3

-- COMMAND ----------

create table oldemp as 
select * from employee version as of 3

-- COMMAND ----------

select * from employee timestamp as of '2023-09-27T08:37:01.000+0000'

-- COMMAND ----------


