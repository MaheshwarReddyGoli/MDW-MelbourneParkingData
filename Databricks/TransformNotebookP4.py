# Databricks notebook source
from pyspark.sql.types import *

# COMMAND ----------

CarParkBayRestrictions_df = spark.read.json("dbfs:/mnt/interim/CarParkBayRestrictions")
CarParkBayRestrictions_df.createOrReplaceTempView("CarParkBayRestrictions_df")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select bayid, 
# MAGIC case
# MAGIC when fromday1 = '0' then "Sunday"
# MAGIC when fromday1 = '1' then "Monday"
# MAGIC when fromday1 = '2' then "Tuesday"
# MAGIC when fromday1 = '3' then "Wednesday"
# MAGIC when fromday1 = '4' then "Thursday"
# MAGIC when fromday1 = '5' then "Friday"
# MAGIC when fromday1 = '6' then "Saturday"
# MAGIC end StartingDay, starttime1 as StartTime,
# MAGIC case 
# MAGIC when today1 = '0' then "Sunday"
# MAGIC when today1 = '1' then "Monday"
# MAGIC when today1 = '2' then "Tuesday"
# MAGIC when today1 = '3' then "Wednesday"
# MAGIC when today1 = '4' then "Thursday"
# MAGIC when today1 = '5' then "Friday"
# MAGIC when today1 = '6' then "Saturday"
# MAGIC end EndingDay,
# MAGIC endtime1 as EndTime, typedesc1 as ParkingType from CarParkBayRestrictions_df where (typedesc1 like "%3P" or typedesc1 like "2P%" and typedesc1 not like "%Disabled%")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select bayid, 
# MAGIC case
# MAGIC when fromday1 = '0' then "Sunday"
# MAGIC when fromday1 = '1' then "Monday"
# MAGIC when fromday1 = '2' then "Tuesday"
# MAGIC when fromday1 = '3' then "Wednesday"
# MAGIC when fromday1 = '4' then "Thursday"
# MAGIC when fromday1 = '5' then "Friday"
# MAGIC when fromday1 = '6' then "Saturday"
# MAGIC end StartingDay, starttime1 as StartTime,
# MAGIC case 
# MAGIC when today1 = '0' then "Sunday"
# MAGIC when today1 = '1' then "Monday"
# MAGIC when today1 = '2' then "Tuesday"
# MAGIC when today1 = '3' then "Wednesday"
# MAGIC when today1 = '4' then "Thursday"
# MAGIC when today1 = '5' then "Friday"
# MAGIC when today1 = '6' then "Saturday"
# MAGIC end EndingDay,
# MAGIC endtime1 as EndTime, typedesc1 as ParkingType from CarParkBayRestrictions_df where (typedesc1 like "4P%" and typedesc1 not like "%Disabled%")

# COMMAND ----------


