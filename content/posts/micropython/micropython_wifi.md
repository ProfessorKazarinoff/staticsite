Title: Connecting to WiFi using Micropython on an Adadfruit Feather Huzzah ESP8266
Date: 2018-07-19 09:01
Modified: 2018-07-19 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, WiFi
Slug: micropython-wifi
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 5
Summary: This is the fifth part of a multipart series on Micropython. In the last post we used the Micropython REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266 board to read the temperature off a temperature sensor. In this post, we are going to connect the Feather board to WiFi and post the temperature to ThingSpeak.com

This is the fifth part of a multipart series on Micropython. In the last post we used the Micropython REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266 board to read the temperature off a temperature sensor. In this post, we are going to connect the Feather board to WiFi and post the temperature to ThingSpeak.com

Before we can connect the Adafruit Feather Huzzah to WiFi, Micropython needs to be installed on the board and Putty needs to be installed to communicate with the board over serial. See a [previous post]({filename}micropython_install.md) to see how to install Micropython on an ESP8266 board and how to install Putty on a Windows 10 machine.

Summary of Steps:

1. Wire up the temperature sensor to the Adafruit Feather Huzzah
2. Connect the Adafruit Feather Huzzah to the computer, open Putty at 115200 baud
3. Run commands at the Micropython REPL to connect the board to WiFi
4. Upload temperature data to ThingSpeak.com

### 1. Wire up the temperature sensor to the Adafruit Feather Huzzah

Wire up the temperature sensor to the Adafruit Feather Huzzah as shown in a [previous post]({filename}micropython_temp_sensor.md)

![Fritzing Diagram]({filename}/posts/micropython/feather_huzzah_temp_sensor_fritzing.png)

### 2. Connect the Adafruit Feather Huzzah ESP8266 board and open Putty

Connect the Feather using a USB data cable. Open Putty. Ensure the serial port is set correctly the baud rate is set to 115200.

![Putty config]({filename}/posts/micropython/putty_config.PNG)

### 3. Run commands at the micropython REPL to connect the board to WiFi

To connect the ESP8266 to a WiFi network, we first need to import the ```network``` module and create an instance of the ```WLAN``` module. Next we use the ```connect``` method and our WiFi network's SSID and password to logon. We want to run our ESP8266 in station mode (like a laptop or phone) as opposed to access point mode (like a server). We can print the IP address of the board using the ```ifconfig()``` method.

```text
>>> import network
>>> sta_if = network.WLAN(network.STA_IF)
>>> sta_if.active(True)
>>> sta_if.connect('SSID', 'password')
>>> print('network config:', sta_if.ifconfig())
```

Now that the board is connected to a WiFi network, we can use the Feather board to read a webpage. Micropython does this with __sockets__ . A socket is a connection between the ESP8266 and the outside internet.

```text
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

Now imagine that our weather station is up and working. It has a temperature sensor and the measured temperature is 21*C. We are going to push this temperature data reading up to ThingSpeak.com. ThingSpeak.com is an internet of things (IoT) cloud provider. We'll  upload the temperature to ThingSpeak.com using an http GET request in the format required by ThingSpeak API.

Sign up for a ThingSpeak.com account and create a new channel. In the channel create a new field called temperture. Note the ThingSpeak channel number and ThingSpeak write API key. Both of these will be needed to send our temperature up to ThingSpeak.

At the Micropython prompt, we'll build a new fuction called ```http_get()``` which will initiate an http GET action by the Feather Board. We can then feed this ```http_get()``` function a specific URL that will activate the ThingSpeak API and post the temperature.

```text
>>> def http_get(url):
...    import socket
...    _, _, host, path = url.split('/', 3)
...    addr = socket.getaddrinfo(host, 80)[0][-1]
...    s = socket.socket()
...    s.connect(addr)
...    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
...    while True:
...        data = s.recv(100)
...        if data:
...            print(str(data, 'utf8'), end='')
...        else:
...            break
```

Now we need to build the URL that will call the ThingSpeak web API. The URL contains four parts: A base domain, an API key, a field number and data. Let's assume our temperature data is 21 (for 21 degrees C). We can build these multiple parts as strings in Micropython and then combine the parts to create one long URL.

```text
>>> base_url = 'https://api.thingspeak.com/update'
>>> API_key = '?api_key=XXXXXXXXXXXXXX'
>>> field = '&field1='
>>> data = '21'
>>> url = base_url + API_key + field + data
```

Now we can use the http_get function and our URL to send the temperature 21 up to ThingSpeak.com

```text
>>> http_get(url)
```

If you go to ThingSpeak.com/<your channel number>, you should see this temperature point. Now let's read an actual temperature off of the temperature sensor and send that value up to ThingSpeak.

```text
>>> import machine
>>> i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4))
>>> byte_data = bytearray(2)
>>> i2c.readfrom_mem_into(24, 5, byte_data)
>>> value = byte_data[0] << 8 | byte_data[1]
>>> temp = (value & 0xFFF) / 16.0
>>> if value & 0x1000:
...     temp -= 256.0
...     print(temp)
>>> base_url = 'https://api.thingspeak.com/update'
>>> API_key = '?api_key=XXXXXXXXXXXXXX'
>>> field = '&field1='
>>> data = str(temp)
>>> url = base_url + API_key + field + data
>>> http_get(url)
```

Another data point should now be up on ThingSpeak.com.

### Next steps

Pretty amazing to have a little piece of hardware like the Feather Huzzah ESP8266 wirelessly upload a temperature measurement. It did require a lot of typing at the Micropython REPL though. In the next post, we'll build a couple of **_.py__** files to save the functions we wrote to read the temperature, build the URL and complete the http GET request.