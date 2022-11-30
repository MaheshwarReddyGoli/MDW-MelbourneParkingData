# MDW-MelbourneParkingData

### Overview
Realtime Melbourne Parking Sensor data from a publicly available REST api endpoint taken as a reference to complete this project, which is then saved to Azure Data Lake Gen2. Stored data is cleansed, and transformed to a known schema using Azure Databricks. A second Azure Databricks job then transforms these into a Star Schema which are then loaded into Azure Synapse Analytics (formerly SQLDW). The entire pipeline is orchestrated with Azure Data Factory.
