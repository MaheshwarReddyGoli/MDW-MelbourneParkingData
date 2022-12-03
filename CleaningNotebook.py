# Databricks notebook source
pip install adlfs

# COMMAND ----------

pip install fsspec

# COMMAND ----------

# importing libraries
import pandas as pd

# COMMAND ----------

# mounting azure blob storage to azue databricks using SAS Token
spark.conf.set("fs.azure.account.auth.type.storagebigfiveproject.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.storagebigfiveproject.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.storagebigfiveproject.dfs.core.windows.net", "sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2022-12-13T13:26:40Z&st=2022-12-03T05:26:40Z&spr=https&sig=NpzxdT1%2BvdxM6iZv6ouzrHA7638zw4gfdki%2BcigIaUE%3D")

# COMMAND ----------

# reading json file form landing zone
ParkingBaySensors_df = spark.read.json("abfs://landing@storagebigfiveproject.dfs.core.windows.net/ParkingBaySensors.json")
CarParkBayRestrictions_df = spark.read.json("abfs://landing@storagebigfiveproject.dfs.core.windows.net/CarParkBayRestrictions.json")

ParkingBaySensors_pdf = ParkingBaySensors_df.toPandas()


# COMMAND ----------

ParkingBaySensors_pdf.isnull().sum()

# COMMAND ----------

ParkingBaySensors_dup_df = ParkingBaySensors_pdf.drop_duplicates(subset=['bay_id'])

# COMMAND ----------

ParkingBaySensors_sdf = ParkingBaySensors_dup_df.dropna()

# COMMAND ----------

ParkingBaySensors_sdf.to_json("abfs://interim@storagebigfiveproject.dfs.core.windows.net/ParkingBaySensors")

# COMMAND ----------


