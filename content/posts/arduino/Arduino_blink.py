# Arduino_blink.py

import serial
import time

for i in range(10):
    with serial.Serial("COM15", 9800, timeout=1) as ser:
        time.sleep(2)
        ser.write(b"H")  # send a byte
        time.sleep(0.5)  # wait 0.5 seconds
        ser.write(b"L")  # send a byte
