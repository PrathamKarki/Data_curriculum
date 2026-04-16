from pyspark.sql import SparkSession 
from pyspark.sql.functions import col, sum, avg, count

# Starting up the spark 
spark = SparkSession.builder.appName("spark_pipeline").getOrCreate()

# creating of the dataset
data = [
    ("IT", "Ram", 1000),
    ("HR", "Sita", 2000),
    ("IT", "Hari", 3000),
    ("FIN", "Gita", 1500),
    ("HR", "John", 2500),
    ("IT", "Asha", 1200)
]

df = spark.createDataFrame(data, ["dept", "Name", "Salary"])

df.show()


# Selecting only needed columns
print("\n Selecting only department and salary")
df.select("dept", "salary").show()


# Filtering data
print("Filtering of salary greater than 1500\n")

df.filter(col("Salary") > 1500).show()


# Adding new columns

print("\nAdding of the new columns\n")
df2 = df.withColumn("Salary_with_bonus", col("salary") + 500)
df2.show()

# Group by and aggreations

print("\n Performing group by and aggregation \n")
grouped_df = df.groupby("dept").agg(
    sum("Salary").alias("total_salary"),
    avg("Salary").alias("average_salary"),
    count("Salary").alias("employee_count")
)

grouped_df.show()


# Sorting results
print("---Sorted by total salary DESC----")
grouped_df.orderBy(col("total_salary").desc()).show()

