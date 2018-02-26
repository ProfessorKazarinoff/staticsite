Title: Connecting to WiFi using Micropython on an Adadfruit Feather Huzzah ESP8266
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, WiFi
Slug: micropython-wifi
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 5

This is the fifth part of a multipart series on Micropython. In the last post we used the Python REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266 board to read the temperature off a temperature sensor. In this post, we are going to connect the Feather board to WiFi and post the temperature to ThingSpeak.com

Before we can connect the Adafruit Feather Huzzah to WiFi, micropython needs to be installed on the board and Putty needs to be installed to communicate with the board over serial. See a [previous post]({filename}micropython_install.md) to install micropython on your board and Putty on a Windows machine.

Summary of Steps:

1. Wire up the temperature sensor to the Adafruit Feather Huzzah
2. Connect the Adafruit Feather Huzzah to the computer, open Putty at 115200 baud
3. Run commands at the Micropython REPL to connect the board to WiFi
4. Upload a piece of data to ThingSpeak.com

### 1. Wire up the temperature sensor to the Adafruit Feather Huzzah

Wire up the temperature sensor to the Adafruit Feather Huzzah as shown in a [previous post]({filename}micropython_temp_sensor.md)

![Fritzing Diagram]({filename}/posts/micropython/fritzing_temp_sensor.png)

### 2. Connect the Adafruit Feather Huzzah ESP8266 board and Open Putty

Connect the Feather using a USB data cable. Open Putty. Ensure the serial port is set correctly the baud rate is set to 115200.

![Putty config]({filename}/posts/micropython/putty_config.PNG)

### 3. Run commands at the micropython REPL to connect the board to WiFi

To connect the ESP8266 to a WiFi network, we first need to import the ```network``` module and create an instance of the ```WLAN``` module. Next we use the ```connect``` method and our WiFi network's SSID and password to logon. We want to run our ESP8266 in station mode (like a laptop or phone) as opposed to access point mode (like a server). We can print the IP address of the board using the ```ifconfig()``` method.

```
>>> import network
>>> sta_if = network.WLAN(network.STA_IF)
>>> sta_if.active(True)
>>> sta_if.connect(SSID, password)
>>> print('network config:', sta_if.ifconfig())
```

Now that we are connected to the network, it what we really want to do is read a webpage. Micropython does this with __sockets__ . A socket is a connection between the ESP8266 and the outside internet. 

```
>>> import socket
>>> url = 'https://google.com'
>>> _, _, host, path = url.split('/', 3)
>>> addr = socket.getaddrinfo(host, 80)[0][-1]
>>> s = socket.socket()
>>> s.connect(addr)
>>> s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
>>> while True:
....   data = s.recv(100)
....   if data:
....       print(str(data, 'utf8'), end='')
....   else:
....       break
```

### 4. Upload to ThingSpeak.com

Now imagine that our weather station is up and workinging. It has a temperature sensor and the measured temperature is 21*C. We are going to push this temperature data reading up to ThingSpeak.com. We will do this using an http GET request in the format of the ThingSpeak API. Sign up for a ThingSpeak.com account and create a new channel. In the channel create a new field called temperture. Note the ThingSpeak channel number and ThingSpeak write API key. Both of these will be needed to send our temperature up to ThingSpeak.