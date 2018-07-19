Title: Upload Micropython Code an Adadfruit Feather Huzzah ESP8266
Date: 2018-07-19 09:01
Modified: 2018-07-19 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller
Slug: micropython-upload-code
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 6

This is the sixth part of a multipart series on Micropython. In this post, we will upload our scripts to the Adafruit Feather Huzzah ESP8266 board using Python and a Python package called **ampy**. At the end of the post we will have a working WiFi Weather station that will post the temperature to ThingSpeak.com

Before we can use the Microython REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266, Micropython needs to be installed on the board and Putty needs to be installed to communicate with the board over serial. See the [previous post]({filename}micropython_install.md) on how to install Micropython on an ESP8266 board and how to install Putty on a Windows 10 machine.

Summary of Steps:

1. Install **ampy** with **pip**
2. Write Python code
3. Put the code on the board with ****ampy
4. Run functions from the micropyton REPL
5. Run a program

### 1. Install **ampy** with **pip**

**Ampy** is a tool written by the folks at Adafruit. **Ampy** is used to upload files on to the ESP8266. Since I'm using a virtual environment, I need to activate the virtual environment before installing **ampy**. Note that the tool is called **ampy**, but we ```pip install ampy-adafruit```

```bash
$ conda activate micropython
(micropython) $ pip install ampy-adafruit
(micropython) $ ampy --help
```

### 2. Write Python Code

Now we need to write the Python code that w'll to put on the ESP8266 board. The board has two main Python files: **_boot.py_** and **_main.py_**. We can also add additional files to the board. **_boot.py_** is the file that runs first when the board is powered up. After **_boot.py_** runs, then **_main.py_** will run. We can add other **_.py_** files to the board to provide **_main.py_** some functions and classes to work with. We have two general things to do with our Feather board, reading temperature and posting it to the ThingSpeak. So let's use two different **.py** files for each of these general functionalities. 

The first **_MCP9808.py_** file will simplify reading temperature data off of the Adafruit MCP9808 temperature breakout. We will write a function that parses out the temperature data from the I2C bus and return it as the output for our ```readtemp()``` function. The function needs to import the ```machine``` module to use the I2C bus. The machine module will allow us to create a new i2c object. When we create the object, we need to specify the ```scl``` and ```sda``` pins that the sensor is connected to. ```scl``` is the i2c clock line and ```sda``` is the i2c data line. These are pins 5 and 4 on the Adafruit Feather Huzzah. Then a new byte array variable needs to be created, so that we can later write data from the sensor into it.  Next we need to read the sensor data using the ```i2c.readfrom_mem_into()``` function. The first argument is the I2C bus address for the sensor. In this case the sensor is at I2C bus address ```24```. You can use the line ```>>> i2c.scan()``` in the Micropython REPL to see this value.  The next function argument is the register on the MCP9808 temperature sensor where the temperature value is stored, which happens to be register ```5```. If we access register ```5``` on the MCP, we will read in the temperature. The third arguments is the variable that we store the temperature data into. The ```i2c.readfrom_mem_into``` function changes the variable that is a function argument, rather than changing a variable which is the function output as most functions do. This is why we need to first create the ```byte_data``` variable before calling the function. Next we need to do some post processing of the byte array to transform it into a temperature in degrees C.

```python
# MCP9808.py

# Functions for the  MCP9808 temperature sensor
# https://learn.adafruit.com/micropython-hardware-i2c-devices/i2c-master

def readtemp():
    import machine
    i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
    byte_data = bytearray(2)
    i2c.readfrom_mem_into(24, 5, byte_data)
    value = byte_data[0] << 8 | byte_data[1]
    temp = (value & 0xFFF) / 16.0
    if value & 0x1000:
        temp -= 256.0
    return temp
```

Now we'll build a Python file for the set of WiFi functions called **_wifitools.py_**. 

```python
#wifitools.py

# Wifi connection and post functions for an ESP8266 board running Micropython
#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_basics.html

def connect(SSID,password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

#https://docs.micropython.org/en/v1.8.6/esp8266/esp8266/tutorial/network_tcp.html
def http_get(url):
    import socket
    _, _, host, path = url.split('/', 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
    while True:
        data = s.recv(100)
        if data:
            print(str(data, 'utf8'), end='')
        else:
            break

def thingspeak_post(API_key,data):
    if not isinstance(data, str):
        data = str(data)
    if not isintance(API_key, str):
        API_key = str(API_key)
    base_url = 'https://api.thingspeak.com/update'
    API_key = '?api_key=' + API_key
    field = '&field1='
    url = base_url + API_key + field + data
    http_get(url)

```

Now let's write a script in a file called **_main.py_** which will use these functions. This **_main.py_** script will import our MCP9808 and wifitools modules and use the ```wifitools.connect()``` function to connect to the WiFi network. There is a ```time.sleep(5)``` line to allow the board time to connect. Next we'll run a loop for a total of 8 hours at 60 minutes in each hour. Inside the loop, we'll read in the temperature from the MCP9808 using the ```MCP9808.readtemp()``` function and post the temperature to ThingSpeak.com using the ```wifitools.thingspeak_post()``` function. To read the temperature once a minute, we need to ```time.sleep(60)``` (wait 60 seconds) between each measurement.

```python
# main.py
# ESP8266 Feather Huzzah Weather Station

import wifitools
import MCP9808
import time
import config

api_key = config.API_KEY
ssid = config.SSID
password = config.WIFI_PASSWORD

wifitools.connect(ssid,password)
time.sleep(5)

for i in range(8*60):
    data = MCP9808.readtemp()
    wifitools.thingspeak_post(api_key,data)
    time.sleep(60)

```

### 3. Upload Python Code to the Feather Huzzah with ampy

Once all the **__.py__** files are created, ensure the Adafruit Feather Huzzah ESP8266 board is connected with a USB cable to the computer. You will also need to know what serial port the Feather board is connected to. We'll upload the code files to the board using ```ampy```. Make sure that you are in the directory with the **_.py_** files and that you are working in the ```(micropython)``` virtual environment that has **ampy** installed in it.

```bash
(micropython)$ ampy --port COM4 put MCP9808.py
(micropython)$ ampy --port COM4 put wifitools.py
(micropython)$ ampy --port COM4 put main.py
(micropython)$ ampy --port COM4 ls
boot.py
wifitools.py
MCP9808.py
config.py
main.py
```

### 4. Unplug and power up the Feather Huzzah and watch the data on ThingSpeak.com

The Feather Huzzah needs to be restarted to run the code we just uploaded. To restart the board unplug and then replug the board's power. Once power is restored, the board will run through the **_boot.py_** script then start the **_main.py_** script. When the board runs the **_main.py_** script, the board will connect to the WiFi network, read the temperature and upload the data to ThingSpeak.com. If we go to ThingSpeak.com, we should see the temperature plotted on our Channel's page.

### Congrats! You have a working weather station that is part of the Internet of Things.

Now you can read the temperature from anywhere with an internet connection.