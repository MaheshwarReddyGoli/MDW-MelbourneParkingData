# Databricks notebook source
# mounting azure blob storage to azue databricks using SAS Token
spark.conf.set("fs.azure.account.auth.type.storagebigfiveproject.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.storagebigfiveproject.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.storagebigfiveproject.dfs.core.windows.net", "sv=2021-06-08&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2022-12-22T02:46:51Z&st=2022-12-03T18:46:51Z&spr=https&sig=ag5mOx7K2Sg%2FcnpBqySOwjWP4MeZzTy3%2FnS7OEFj93s%3D")

# COMMAND ----------

# reading json file form landing zone
parkingbaysensors_df = spark.read.json("abfs://bigfiveproject@storagebigfiveproject.dfs.core.windows.net/landing/ParkingBaySensors.json")
carparkbayrestrictions_df = spark.read.json("abfs://bigfiveproject@storagebigfiveproject.dfs.core.windows.net/landing/CarParkBayRestrictions.json")

# COMMAND ----------

# Cleaning data by dropDuplicates to remove duplicates
parkingbaysensors_sdf = parkingbaysensors_df.dropDuplicates()
carparkbayrestrictions_sdf = carparkbayrestrictions_df.dropDuplicates()

# COMMAND ----------

# Write cleaned data into interim folder
parkingbaysensors_sdf.coalesce(1).write.json("abfs://bigfiveproject@bigfiveprojectstorage.dfs.core.windows.net/interim/parkingbaysensors")
# parkingbays_sdf.coalesce(1).write.json("abfs://melbourne@bigfiveprojectstorage.dfs.core.windows.net/interim/parkingbays")
carparkbayrestrictions_sdf.coalesce(1).write.json("abfs://bigfiveproject@bigfiveprojectstorage.dfs.core.windows.net/interim/carparkbayrestrictions")
# parkingbaysensors_sdf.coalesce(1).write.format('json').save("abfs://melbourne@bigfiveprojectstorage.dfs.core.windows.net/interim/test")

# COMMAND ----------

#parkingbaysensors_sdf.write.format('json').mode("overwrite").option("header","true").save("abfs://melbourne@storagebigfiveproject.dfs.core.windows.net/interim/parkingbaysensors")
#parkingbays_sdf.write.format('json').mode("overwrite").option("header","true").save("abfs://melbourne@storagebigfiveproject.dfs.core.windows.net/interim/parkingbays")
#carparkbayrestrictions_sdf.write.format('json').mode("overwrite").option("header","true").save("abfs://melbourne@storagebigfiveproject.dfs.core.windows.net/interim/carparkbayrestrictions")
