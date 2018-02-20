Title: Connecting to WiFi using Micropython on an Adadfruit Feather Huzzah ESP8266
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller
Slug: micropython-wifi
Authors: Peter D. Kazarinoff
Series: micropython
series_index:3

This is the third part of a multipart series on Micropython. In the last post we used the Python REPL (the Python prompt) running on the Adafruit Feather Huzzah ESP8266 board to turn on and off an LED. In this post, we are going to connect the Feather board to WiFi.

Before we can connect the Adafruit Feather Huzzah to WiFi, micropython needs to be installed on the board and Putty needs to be installed to communicate with the board over serial. See a [previous post]({filename}micropython_install.md) to install micropython on your board and Putty on a Windows machine.

Summary of Steps:

1. Connect Adafruit Feather Huzzah, open Putty at 115200 baud
2. Run commands at the micropython REPL to connect the board to WiFi
3. Upload a piece of data to ThingSpeak.com

### 1. Connect the Adafruit Feather Huzzah ESP8266 board and Open Putty

Connect the Feather using a USB data cable. Open Putty. Ensure the serial port is set correctly the baud rate is set to 115200.

![Putty config]({filename}/posts/micropython/putty_config.PNG)

### 2. Run commands at the micropython REPL to connect the board to WiFi

To connect the ESP8266 to a WiFi network, we first need to import the ```network``` module and create an instance of the ```WLAN``` module. 

```
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
```

### 3. Upload to ThingSpeak.com

