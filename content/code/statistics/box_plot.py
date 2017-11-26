from statistics import mean, median, mode, stdev
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data1 = [83,83,93,91,85,64,79,97,95,67,83,90,92,73,82,85,96,84,82,71,86,68,66,95,87,81,77,81,97]
data2 = [60,79,89,97,68,82,67,59,77,87,99,102,73,78,91,89,84,81,78,90,92,97,82]
data3 = [85,94,100,100,47,78,100,92,49,86,90,100,84,89,82,100,100,100,96,82,65,92,96,85,76,100,90,100]
data4 = [79,100,90,82,76,90,86,88,86,93,99,92,84,77,100,100,96,93,91,86,74,74,100,93,69,89,93,100]
data = data1 + data2 + data3 + data4

data_mean = mean(data)
data_median = median(data)
try:
    data_mode = mode(data)
except:
    data_mode = 'None'
data_stdev = stdev(data)

print('mean: %4.1f' %data_mean)
print('median: %4.1f' %data_median)
print('mode: %s' %data_mode)
print('std dev: %4.1f ' %data_stdev)

plt.hist(data)
plt.xlabel('Grade Range')
plt.ylabel('Number of Students')
plt.title('Historgram of ENGR101 Exam Grades')
plt.show()
