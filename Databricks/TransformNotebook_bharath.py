# Databricks notebook source
from pyspark.sql.types import *

# COMMAND ----------

adlsAccountName = "storagebigfiveproject"
adlsContainerName = "bigfiveproject"
adlsFolderName = "landing"
mountPoint = "/mnt/final"

applicationId = dbutils.secrets.get(scope="Secret01", key="appid")

authenticationKey = dbutils.secrets.get(scope="Secret01",key="clientsecret")

tenandId = dbutils.secrets.get(scope="Secret01",key="tenantid")

endpoint = "https://login.microsoftonline.com/" + tenandId + "/oauth2/token"
source = "abfss://" + adlsContainerName + "@" + adlsAccountName + ".dfs.core.windows.net/" + adlsFolderName

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": applicationId,
           "fs.azure.account.oauth2.client.secret": authenticationKey,
           "fs.azure.account.oauth2.client.endpoint": endpoint}

if not any(mount.mountPoint == mountPoint for mount in dbutils.fs.mounts()):
  dbutils.fs.mount(
    source = source,
    mount_point = mountPoint,
    extra_configs = configs)

# COMMAND ----------

ParkingBaySensors_df = spark.read.json("dbfs:/mnt/interim/ParkingBaySensor")
CarParkBayRestrictions_df = spark.read.json("dbfs:/mnt/interim/CarParkBayRestrictions")

# COMMAND ----------

ParkingBaySensors_df.createOrReplaceTempView("ParkingBaySensors_df")
CarParkBayRestrictions_df.createOrReplaceTempView("CarParkBayRestrictions_df")

# COMMAND ----------

DF1 = ParkingBaySensors_df.withColumn("lat", ParkingBaySensors_df["lat"].cast(DecimalType(12,2)))
DF2 = DF1.withColumn("lon", DF1["lon"].cast(DecimalType(12,2)))
DF2.createOrReplaceTempView("DF2")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select * from DF2

# COMMAND ----------

# MAGIC %sql
# MAGIC select bay_id, lat, lon from DF2 where status = "Unoccupied"
