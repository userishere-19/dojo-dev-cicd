# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "0d079525-891b-4ece-aad0-8ca05c73bb29",
# META       "default_lakehouse_name": "CD007_Lakehouse",
# META       "default_lakehouse_workspace_id": "4947c88d-a8d8-46a5-b70f-ad81c1f79992",
# META       "known_lakehouses": [
# META         {
# META           "id": "0d079525-891b-4ece-aad0-8ca05c73bb29"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC -- Create DimProduct table
# MAGIC CREATE TABLE DimProduct (
# MAGIC     ProductKey INT,
# MAGIC     ProductName STRING,
# MAGIC     ProductCategory STRING,
# MAGIC     ProductSubcategory STRING,
# MAGIC     Manufacturer STRING
# MAGIC );
# MAGIC 
# MAGIC -- Insert data into DimProduct
# MAGIC INSERT INTO DimProduct VALUES 
# MAGIC (1, 'Laptop', 'Electronics', 'Computers', 'TechCo'),
# MAGIC (2, 'Smartphone', 'Electronics', 'Mobile Phones', 'PhoneCorp'),
# MAGIC (3, 'Headphones', 'Electronics', 'Audio', 'SoundInc');


# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
