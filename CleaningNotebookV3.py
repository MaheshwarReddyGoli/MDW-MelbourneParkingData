# Databricks notebook source
adlsAccountName = "storagebigfiveproject"
adlsContainerName = "bigfiveproject"
adlsFolderName = "landing"
mountPoint = "/mnt/landing"

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

adlsAccountName = "storagebigfiveproject"
adlsContainerName = "bigfiveproject"
adlsFolderName = "interim"
mountPoint = "/mnt/interim"

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

ParkingBaySensors_df = spark.read.json("dbfs:/mnt/landing/ParkingBaySensors.json")
CarParkBayRestrictions_df = spark.read.json("dbfs:/mnt/landing/CarParkBayRestrictions.json")

# COMMAND ----------

display(ParkingBaySensors_df)

# COMMAND ----------

display(CarParkBayRestrictions_df)

# COMMAND ----------

ParkingBaySensors_dup_df = ParkingBaySensors_df.drop_duplicates(subset=['bay_id'])
CarParkBayRestrictions_sdf = CarParkBayRestrictions_df.drop_duplicates(subset=['bayid'])

# COMMAND ----------

ParkingBaySensors_sdf = ParkingBaySensors_dup_df.dropna()

# COMMAND ----------

ParkingBaySensors_sdf.write.format("json").mode("overwrite").save("dbfs:/mnt/interim/ParkingBaySensor")
CarParkBayRestrictions_sdf.write.format("json").mode("overwrite").save("dbfs:/mnt/interim/CarParkBayRestrictions")
