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

This is the fourth part of a multipart series on Micropython. In this last post of the series, we blinked an LED on and off using Micropython. In this post, we will connect a temperature sensor to an Adafruit Feather Huzzah and use the Micropython REPL to read the temperature.

Before we can use the Python REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266, micropython needs to be installed on the board and Putty needs to be installed to communicate with the board over serial. See a [previous post]({filename}micropython_install.md) to install micropython on your board and Putty on a Windows machine.

Summary of Steps:

1. Connect the temperature sensor to the Adafruit Feather Huzzah board
2. Connect the Adafruit Feather Huzzah to the computer with a USB cable and bring up the Micropython REPL using Putty. 
3. Run code at the Micropython REPL to read the temperature


### 1. Connect the temperature sensor to the Adafruit Feather Huzzah board

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