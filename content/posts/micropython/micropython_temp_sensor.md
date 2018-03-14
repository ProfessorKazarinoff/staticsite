Title: Using a Temperature Sensor with Micropython running on an Adadfruit Feather Huzzah ESP8266
Date: 2018-02-26 09:01
Modified: 2018-02-26 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller
Slug: micropython-temp-sensor
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 4

This is the fourth part of a multipart series on Micropython. In this last post of the series, we blinked an LED on and off using Micropython. In this post, we will connect a temperature sensor to an Adafruit Feather Huzzah and use the Micropython REPL to read the temperature. The posts in this series:

1. [What is Micropython?]({filename}what_is_micropython.md)
2. [Installing Micropython on an Adafruit Feather Huzzah ESP8266]({filename}micropython_install.md)
3. [Blink an LED on an Adafruit Feather Huzzah ESP8266 using Micropython]({filename}micropython_REPL.md)
4. Read the temperature from a MCP9808 breakout board using Micropyton (this post)
5. Use Micropython to connect an Adafruit Feather Huzzah to a WiFi network
6. Upload Micropython code to turn an Adafruit Feather Huzzah into a WiFi-enabled IoT weather station
7. Use **pandas** and **matplotlib** to plot the weather data from a WiFi-enabled IoT weather station.
8. Upload MicroPython to a cheap $3 ESP-01 module
9. Build custom firmware to turn the $3 ESP-01 into an low-cost WiFi enabled IoT switch.

Before we can use the temperature sensor running on the Adafruit Feather Huzzah ESP8266, Micropython needs to be installed on the board and Putty needs to be installed to communicate with the board over serial. See a [previous post]({filename}micropython_install.md) to install micropython on your board and Putty on a Windows machine.

Summary of Steps:

1. Connect the temperature sensor to the Adafruit Feather Huzzah board
2. Connect the Adafruit Feather Huzzah to the computer with a USB cable and bring up the Micropython REPL using Putty. 
3. Run code at the Micropython REPL to read the temperature


### 1. Connect the temperature sensor to the Adafruit Feather Huzzah board

Connect the temperature sensor to the feather huzzah board with jumper wires. There needs to be four connections: The I2C data and clock lines, plus power and ground. 
![Fritzing Image]({filename}/posts/micropython/fritzing_image.png)

### 2. Connect the Adafruit Feather Huzzah to the computer with a USB cable and bring up the Micropython REPL using Putty.

### 3. Run code at the Micropython REPL to read the temperature

```
>>> import machine
>>> i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
>>> byte_data = bytearray(2)
>>> i2c.readfrom_mem_into(24, 5, byte_data)
>>> value = byte_data[0] << 8 | byte_data[1]
>>> temp = (value & 0xFFF) / 16.0
>>> if value & 0x1000:
...     temp -= 256.0
.....   print(temp)
```

## Next steps:
Connect the Adafruit Feather Huzzah to WiFi and upload the temperature data to ThingSpeak.com.
