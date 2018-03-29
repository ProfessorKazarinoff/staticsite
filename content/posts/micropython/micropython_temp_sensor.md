Title: Using a Temperature Sensor with Micropython running on an Adadfruit Feather Huzzah ESP8266
Date: 2018-03-28 09:01
Modified: 2018-03-28 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, sensor
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

Before we can use the [MCP9808 temperature sensor](https://www.adafruit.com/product/1782) running on the Adafruit Feather Huzzah ESP8266, Micropython needs to be installed on the board and Putty needs to be installed in Windows 10 to communicate with the board over serial. See a [previous post]({filename}micropython_install.md) to install Micropython on your board and Putty on a Windows machine.

Summary of Steps:

1. Connect the temperature sensor to the Adafruit Feather Huzzah board
2. Connect the Adafruit Feather Huzzah to the computer with a USB cable and bring up the Micropython REPL using Putty. 
3. Run code at the Micropython REPL to read the temperature


### 1. Connect the MCP9808 temperature sensor to the Adafruit Feather Huzzah board

Connect the [MCP9808 temperature sensor](https://www.adafruit.com/product/1782) breakout board to the Feather Huzzah board with jumper wires. There are four connections: A 3V power line from the Feather Huzzah to the MCP9808 Vdd pin, GND connected between both boards, and the I2C data and clock lines. On the Feather Huzzah, the I2C data line is SDA (pin 4) and the I2C clock line is SCL (pin 5). These connect with the MPC9808 I2C data line SDA and the MPC9808 I2C clock line SCL. Unlike Serial communication where RX connects to TX, in I2C SDA connects to SDA and SCL connects to SCL.

| Feather Huzzah | wire | MCP9808 |
| --- | --- | --- |
| 3V | red | Vdd |
| GND | black | GND |
| SDA | green | SDA |
| SCL | yellow | SCL |

![Fritzing Image]({filename}/posts/micropython/feather_huzzah_temp_sensor_fritzing.png)

### 2. Connect the Adafruit Feather Huzzah to the computer with a USB cable and bring up the Micropython REPL using Putty.

Connect the Adafruit Feather Huzzah to the computer with a microUSB cable. Ensure this is a data cable, not just a charging cable. Open Putty and connect to the Feather Huzzah using the proper serial port (COM#) and 115200 baud. (Remember to use the **Serial** radio button under **Connection Type:**)

![Putty in start menu]({filename}/posts/micropython/putty_in_start_menu.png)

![Putty config]({filename}/posts/micropython/putty_config.PNG)

This should bring up the Micropython REPL prompt ```>>>```. If you can't see the ```>>>``` prompt, try typing [Enter], Ctrl-D, pushing the RESET button on the Feather Huzzah. If that doesn't work, try closing putty then unplugging then replugging the USB cable.

### 3. Run code at the Micropython REPL to read the temperature

In the Putty Serial Window, we will import the ```machine``` module and then create an instance of the ```machine.I2C``` class with the scl and sda parameters set as ```scl=machine.Pin(5)``` and ```sda=machine.Pin(4)```.  Then we create an empty ```bytearray``` which will be used to store the data coming in from the MCP9808 temperature sensor. As strings in Micropython are UTF-8 encoded by defaut, like in Python 3, a bytearray needs to be used to read the raw output from the MCP9808 chip registers. The command ```i2c.readfrom_mem_into()``` method brings in the data from the sensor and saves it to our ```byte_data``` variable. The arguments inside the method ```24``` and ```5``` correspond to the I2C memory address and registry address of the temperature data stored in the MCP9808 temperature sensor.   

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
In the next post we will use Micropython to connect the Adafruit Feather Huzzah to a WiFi network.
