# potentiometer.py

import serial
import time

ser = serial.Serial('COM15', 9800, timeout=1)
time.sleep(2)

for i in range(50):
    line = ser.readline()   # read a '\n' terminated line
    if line:
        string = line.decode()  # convert the byte string to a unicode string
        num = int(string) # convert the unicode string to an int
        print(num)

ser.close()
