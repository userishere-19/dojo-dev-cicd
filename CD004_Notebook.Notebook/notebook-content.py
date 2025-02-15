# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "e2516baf-7af5-4231-9333-c5e936413902",
# META       "default_lakehouse_name": "CD004_LH1",
# META       "default_lakehouse_workspace_id": "4947c88d-a8d8-46a5-b70f-ad81c1f79992",
# META       "known_lakehouses": [
# META         {
# META           "id": "e2516baf-7af5-4231-9333-c5e936413902"
# META         },
# META         {
# META           "id": "0ae5e252-1c73-4a70-9b77-ff8f91c92d62"
# META         }
# META       ]
# META     },
# META     "environment": {
# META       "environmentId": "bafa9be4-5cf9-aa54-42f1-1e845672e418",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# PARAMETERS CELL ********************

my_parameter = 1

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
print('Hello World')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sparkr
# MAGIC print('Hello World')


# METADATA ********************

# META {
# META   "language": "r",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * FROM companies

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
