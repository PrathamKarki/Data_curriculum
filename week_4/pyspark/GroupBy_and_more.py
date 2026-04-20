from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count

spark = SparkSession.builder.appName("groupby_practice").getOrCreate()

data = [
    ("IT", 1000),
    ("HR", 2000),
    ("IT", 3000),
    ("FIN", 3000),
    ("HR", 1500),
    ("IT", 1200)
]

df = spark.createDataFrame(data, ["dept", "salary"])

df.show()

# Understanding the groupby operations


# Total salary per department
df.groupBy("dept").sum("salary").show()

# Average salary per department
df.groupBy("dept").avg("salary").show()

# Count employees per department
df.groupBy("dept").count().show()


# Renaming of the aggregated columns

df.groupBy("dept").agg(
    sum("salary").alias("Total_salary")
).show()

# Multiple aggregation

df.groupBy("dept").agg(
    sum("salary").alias("total_salary"),
    avg("salary").alias("avg_salary"),
    count("salary").alias("employee_count")
).show()


# filtering after the groupby
grouped = df.groupBy("dept").agg(
    sum("salary").alias("total_salary")
)

grouped.filter(col("total_salary") > 4000).show()