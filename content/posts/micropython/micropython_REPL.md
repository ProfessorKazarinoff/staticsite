Title: Using the Micropython RERL on an Adadfruit Feather Huzzah ESP8266
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller
Slug: micropython-install
Authors: Peter D. Kazarinoff
Series: micropython
series_index:1

This is the second part of a multipart series on Micropython. In this first post, we installed micropython on an Adafruit Feather Huzzah ESP8266 board using Python and an package called esptool. In this post, we are going to write commands to the Python REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266 board to turn on and off an LED.

Before we can use the Python REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266, micro python needs to be installed on the board and Putty needs to be installed to communicate with it over serial. See the [previous post]({filename}micropython_install.md) to prepare your board and Windows machine.

Summary of Steps:

1. Connect Adafruit Feather Huzzah ESP8266 using a USB cable
2. Determine which COM port the board is connected to using the Windows Device Manager 
3. Open Putty and connect to the board at 115200 baud
4. Run commands at the prompt to turn the builtin LED on the Adafruit Feather Huzzah ESP8266

### 1. Connect the Adafruit Feather Huzzah ESP8266 board to the laptop

Use a microUSB cable to connect the Feather Huzzah to the computer. Make sure that the microUSB cable is a full USB data cable and not just a simple power cable. 

### 2. Determine the Serial port that the Feather Huzzah is connected to

Use Windows device manager to determine which serial port the Feather Huzzah is connected to. On my Windows 10 laptop, it usually comes up as ```COM4```.

![Find Device Manager]({filename}/posts/micropython/find_device_manager.png)

![Device Manager Menu]({filename}/posts/micropython/device_manager_menu.png)

### 3. Use Putty to connect to the Feather Huzzah

Ensure the Feather is connected with a USB cable, and connect with Putty using the proper serial port and 115200 baud.

![Putty in start menu]({filename}/posts/micropython/putty_in_start_menu.png)

![Putty config]({filename}/posts/micropython/putty_config.PNG)

![REPL prompt]({filename}/posts/micropython/REPL_prompt.PNG)


### 4. Run commands at the prompt to turn the builtin LED on the Adafruit Feather Huzzah ESP8266

At the command prompt try the following commands

```
>>> print('Micropython for Engineers!')
Micropython for Engineers
```

```
>>> import sys
>>> sys.implementation
(name='micropython', version=(1, 9, 3))
>>> sys.platform
'esp8266'
```

![REPL prompt]({filename}/posts/micropython/sys_dot_implementation_and_platform.PNG)

No let's turn the built-in LED on and off. We do this with the machine module.

```
import machine
machine.Pin(   )
LED.on()
LED.off()

```
## Next steps:
Use the Python REPL on the Adafruit Feather Huzzah to connect to a I2C temperature sensor and read out the temperature.