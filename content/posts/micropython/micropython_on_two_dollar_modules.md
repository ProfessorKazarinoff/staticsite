Title: Micropython on Two Dollar ESP8266-01 Modules
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller
Slug: micropython-on-cheap-modules
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 7

This is the seventh part of a multipart series on Micropython. In this last post of the series, we will upload our scripts to the Adafruit Feather Huzzah ESP8266 board using Python and a package called ampy. In this post we are going to upload micropython on a cheap $2 esp8266-01 board with only 512 kB of flash memory. It is pretty amazing that even these inexpensive boards can run micropython. There are a couple tricks I learned along the way that I wanted to share.

Before we can use upload micropython to our cheap little board, Python and esptool need to be installed on your laptop. I also used a breadboard an FTDI serial adapter and power supply. A little breadboard adapter was supper helpful and made it easy to break out all of the ESP module's pins which are not breadboard friendly on their own.

Summary of Steps:

1. Hook up ESP-01 in regular running mode (GP0,RST-->3.3V) and test, turn off power
2. Hook up ESP-01 in bootloader mode(GP0->>GND), turn on power, touch RST to ground, then unplug RST
3. use esptool to flash memory
4. use esptool to write to flash memory
5. test in putty
6. wire up LED, test in putty

### 1. Hook up ESP-01 in regular running mode (GP0,RST-->3.3V) and test, turn off power

Materials:

ESP-01 module: http://a.co/iFkFL7e
breakout boards: http://a.co/8ENtenc
breadboard power supply: http://a.co/6Jxfyfw - wish these had micro usb, not big usb
FTDI serial to microUSB adaptor: http://a.co/j4WGbT3 - wish this could power ESP-01 on it's own
Breadboard: various
Jumper Wires: various. Better quality is worth it.

A couple things I learned along the way:

For regular running mode, pins from the ESP-01 need to be connected to:

| ESP-01 Pin | 
| --- | ---|
| RST | 3.3V |
| GP0 | 3.3V |
| VC  | 3.3V |
| GND | GND  |
| TX  | TX   |
| RX  | RX   |

* Using a breadboard power supply works better than using power from the FTDI adapter
* The FTDI adapter only has TX, RX and GND connected
* The right angle ESP-01 breakouts are better than the parallel ESP-01 breakouts
* Putty doesn't seem to work. Needed to use the Arduino IDE serial monitor
* need to get COM Port from the Windows Device Manager

```
AT

AT + GMR

AT + RST

```

## Next steps:
Next we'll see if we can turn the LED on and off using WiFi. 