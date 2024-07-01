# Databricks notebook source
configs = {
  "fs.azure.account.auth.type": "OAuth",
  "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id": "ac9ac501-13a5-4fad-b279-fe13e84ae3a9",
  "fs.azure.account.oauth2.client.secret": 'JmU8Q~NsZmH2V.QKfHJ3WwvC.y6mGfbNUeonKbSL',
  "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/7b5ad673-1d69-44b4-8c86-d2bfefbf296c/oauth2/token"
  }

# COMMAND ----------

dbutils.fs.mount(
      source="abfss://tokyo-olympic-data@tokyoolympicdatapro.dfs.core.windows.net",
      mount_point= "/mnt/tokyoolympic",
      extra_configs= configs
  )

# COMMAND ----------

# MAGIC %fs
# MAGIC ls "/mnt/tokyoolympic"

# COMMAND ----------

athletes = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympic/raw-data/athelets.csv")
coaches = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympic/raw-data/coaches.csv")
teams = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympic/raw-data/teams.csv")
medals = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympic/raw-data/medals.csv")
entriesgender = spark.read.format("csv").option("header","true").option("inferSchema","true").load("/mnt/tokyoolympic/raw-data/genders.csv")

# COMMAND ----------

athletes.display();
coaches.display();
teams.display();
entriesgender.display();
medals.display();

# COMMAND ----------

athletes.createOrReplaceTempView("athletes");
coaches.createOrReplaceTempView("coaches");
teams.createOrReplaceTempView("teams");
medals.createOrReplaceTempView("medals");
entriesgender.createOrReplaceTempView("entriesgender")

# COMMAND ----------

from pyspark.sql.functions import initcap

athletes = athletes.withColumn("Name", initcap(athletes.Name))
athletes = athletes.withColumnRenamed("NOC", "Country")
athletes.display()

# COMMAND ----------

from pyspark.sql.functions import initcap

coaches = coaches.withColumn("Name", initcap(coaches.Name))
coaches = coaches.withColumnRenamed("NOC", "Country")
coaches.display()

# COMMAND ----------

teams = teams.drop("Name")
teams = teams.withColumnRenamed("NOC", "Country")
teams.display()

# COMMAND ----------

medals = medals.withColumnRenamed("Team/NOC", "Country")
medals.display()

# COMMAND ----------

athletes.write.format("csv").option("header", "true").mode("overwrite").save("/mnt/tokyoolympic/processed-data/athletes")
coaches.write.format("csv").option("header", "true").mode("overwrite").save("/mnt/tokyoolympic/processed-data/coaches")
teams.write.format("csv").option("header", "true").mode("overwrite").save("/mnt/tokyoolympic/processed-data/teams")
medals.write.format("csv").option("header", "true").mode("overwrite").save("/mnt/tokyoolympic/processed-data/medals")
entriesgender.write.format("csv").option("header", "true").mode("overwrite").save("/mnt/tokyoolympic/processed-data/entriesgender")

# COMMAND ----------


