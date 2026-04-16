from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# creating the spark
spark = SparkSession.builder.appName("basic_practice").getOrCreate()

# Creating of the dataFrame and displaying them
data = [('Ram', 25, 'Kathmandu'), ('Sita', 22, 'Pokhara'), ('Hari', 30, 'Kathmandu'), ('Gita', 28, 'Lalitpur')]


students_data = spark.createDataFrame(data,["Name", "Age", "City"])

displaying_students = students_data.show()
print(displaying_students)


# Selecting of the columns
showCity_and_name = students_data.select("Name", "City").show()

print(showCity_and_name)


# Filtering of the Data

filter_age_and_city = students_data.filter(
    (col("Age") > 25) & (col("City") == "Kathmandu")
).show()

filter_city = students_data.filter(students_data.City == 'Kathmandu').show()
print(filter_city)
print(filter_age_and_city)


# Adding of new columns: age_after_10_years
more_students_data = students_data.withColumn("age_after_10_years", col("age")+10)

print(more_students_data.show())

