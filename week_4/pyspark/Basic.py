from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Basics").getOrCreate()

# Creating DataFrame in pyspark

data = [('Asha', 22), ("Ram", 25), ("Sita", 30)]

df = spark.createDataFrame(data, ["name", "age"])

print(df.show())


# Creating another dataframe in pyspark 
students = [("Harold", 22),  ("Harry", 24), ("Jason", 26), ("Migalda", 21), ("Ronny", 27)]
students_df = spark.createDataFrame(students, ["name", "age"])

print(students_df.show())


# Selecting of the columns
selectName = students_df.select("name").show()
print(selectName)

# Filtering of the data
filterAge = students_df.filter(students_df.age > 24).show()
print(filterAge)


# Adding of the new columns
students_df_2 = students_df.withColumn("age after 5 years", col("age")+ 5)
students_df_2.show()

print(students_df_2.show())