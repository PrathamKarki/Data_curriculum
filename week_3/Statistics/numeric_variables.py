import pandas as pd
import statistics as stats

# Learning about different numeric variables 
# mean, median, and more

data = [10, 20 , 20 , 40 , 50, 100]

print("Data are:", data)

# mean 
mean = stats.mean(data)
print('the mean data is: ', mean)

# median 
median = stats.median(data)
print('the median data is: ', median)

# mode 
mode = stats.mode(data)
print("mode:", mode)

# variance and standard deviations

variance = stats.variance(data)
stand_dev = stats.stdev(data)

print('The variance for the given data is',variance)
print('The standard_dev for the given data is',stand_dev)


# working on with the others data

datas = [5, 5, 5, 5, 5]

mean_value = stats.mean(datas)
median_value = stats.median(datas)
mode_value = stats.mode(datas)
variance_value = stats.variance(datas)
standard_dev_val = stats.stdev(datas)

print("mean is", mean_value)
print("median is", median_value)
print("mode is", mode_value)
print("variance is", variance_value)
print("standard dev value is", standard_dev_val)