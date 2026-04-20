from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Intro").getOrCreate()

print(spark)