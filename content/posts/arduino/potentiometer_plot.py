# potentiometer_plot.py

import serial
import time
import matplotlib.pyplot as plt

ser = serial.Serial('COM15', 9800, timeout=1)
time.sleep(2)

data = []
for i in range(50):
    line = ser.readline()   # read a '\n' terminated line
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int
        print(num)
        data.append(num)
ser.close()

# build the plot
plt.plot(data)
plt.xlabel('Time')
plt.ylabel('Potentiometer Reading')
plt.title('Potentiometer Reading vs. Time')
plt.show()
