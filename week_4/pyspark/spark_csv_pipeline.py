from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count

# Starting the spark
spark = SparkSession.builder.appName("CSV Pipeline").getOrCreate()

# Read the CSV
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

print("\n Printing Raw Data")
df.show()

# Printing of the schema
print("\n Printing of the Schema")
df.printSchema()

# Selecting only name and salary
df_selected = df.select("name", "salary")

df_selected.show()


# Filtering of the data (salary > 1500)
df_filtered = df.filter(col("salary") > 1500)
print("\n Filtered Data")
df_filtered.show()


# Adding of new columns
df_transformed = df_filtered.withColumn("Bonus_salary", col("salary") + 500)

df_transformed.show()

# Group by (aggregation )

print("\nAggregated Data\n")

df_grouped = df_transformed.groupBy("dept").agg(
    sum("Bonus_salary").alias("total_salary"),
    avg("Bonus_salary").alias("avg_salary"),
    count("*").alias("employee_count")
)

df_grouped.show()


# Sort result
df_grouped.orderBy(col("total_salary").desc()).show()