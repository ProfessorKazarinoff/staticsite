Title: Upload Micropython Code an Adadfruit Feather Huzzah ESP8266
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller
Slug: micropython-upload-code
Authors: Peter D. Kazarinoff
Series: micropython
series_index:5

This is the fifth part of a multipart series on Micropython. In this last post of the series, we will upload our scripts to the Adafruit Feather Huzzah ESP8266 board using Python and a package called ampy. At the end of the post we will have a working WiFi Weather station that will post the temperature to ThingSpeak.com

Before we can use the Python REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266, micropython needs to be installed on the board and Putty needs to be installed to communicate with the board over serial. See the [previous post]({filename}micropython_install.md) to install micropython on your board and Putty on a Windows machine.

Summary of Steps:

1. Install ampy with pip
2. Write python code 
3. Put the code on the board with ampy
4. Run functions from the micropyton REPL
5. Run a program

### 1. Install ampy with pip

```
pip install ampy-adafruit
```

### 2. Write Python Code

Now we need to write the Python code that we are going to put on the board. The board has two main Python files: **boot.py** and **main.py**. We can also add additional files to the board. **boot.py** is the file that runs first when the board is powered up. After **boot.py** runs, then **main.py** will run. 

### 3. Upload Python Code to the Feather Huzzah with ampy

Ensure the Feather is connected with a USB cable, and you know what serial port the feather is connected to.

```
ampy --port COM4 put WiFitools.py
ampy --port COM4 put 

```

```
(micropython) C:\Users\Peter\Documents\staticsite\content\code\micropython>ampy --port COM4 put main.py

(micropython) C:\Users\Peter\Documents\staticsite\content\code\micropython>ampy --port COM4 ls
boot.py
wifitools.py
MCP9808.py
config.py
main.py

(micropython) C:\Users\Peter\Documents\staticsite\content\code\micropython>
```

### 4. Run commands at the prompt to turn the built-in LED on the Adafruit Feather Huzzah ESP8266

At the micropython REPL (the micropython command promt) try the following commands:

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

Now let's turn the built-in LED on and off. We do this with the ```machine``` module. We use the ```machine``` module to create a ```Pin``` object. The first argument is the pin number on the board. Pin zero on the Feather Huzzah is connected to the built-in LED. The second argument is the pin type. We want pin zero to act as an ouput pin. We are going to assing it on or off and this will output a positive voltage or no voltage to turn the built-in LED on and off.

```
>>> import machine
>>> pin = machine.Pin(0, machine.Pin.OUT)
```

Pin 0 on the Adafruit Feather Huzzah ESP8266 is kind of wired "backwards". We call ```pin.off()``` to turn the built-in LED **on** and call ```pin.on()``` to turn the built-in LED **off**. 

```
>>> LED.on()
>>> LED.off()
```

Now let's see if we can make the LED blink. We'll do this with a simple ```for``` loop. At the micropython REPL, initiating a loop will automatically indent the next line, so a tab is not needed before the ```print``` statement. To run the loop, we type backspace on an empty line (to backspace from an indented line) and type return.

```
>>> import time
>>> for i in range(10):
...     pin.on()
...     time.sleep(1)
...     pin.off()
...     time.sleep(1)
...
```

This will blink the LED on and off for a total of 20 seconds.

## Next steps:
Use the Python REPL on the Adafruit Feather Huzzah to connect to a I2C temperature sensor and read out the temperature.