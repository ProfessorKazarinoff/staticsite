from statistics import mean, median, mode, stdev
import matplotlib.pyplot as plt

plt.style.use('seaborn')

data1 = [1001.6, 931.5, 1036.4, 990.7, 979.4, 1021.5, 906.8 ]
data2 = [981.7, 919.1, 998.6, 950.0, 940.7, 912.0, 836.9]
data3 = [877.5, 962.7, 997.6, 1094.6, 921.6, 939.4, 898.6]
data4 = [980.0, 859.8, 944.1, 984.3, 1176.8, 987.6, 1023.4]
data5 = [941.8, 1067.5, 1071.3, 958.8, 1115.9, 1055.4, 1027.4]
data = data1 + data2 + data3 + data4 + data5

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
plt.show()