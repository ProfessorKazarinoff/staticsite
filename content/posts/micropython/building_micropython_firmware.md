Title: Building Micropython Firmware for Two Dollar ESP8266-01 Modules
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, firmware
Slug: micropython-on-cheap-modules
Authors: Peter D. Kazarinoff
Series: micropython
series_index:8

This is the eighth part of a multipart series on Micropython. In this last post of the series, we will uploaded micropython on a cheap $2 esp8266-01 board with only 512 kB of flash memory. It was pretty amazing that even these inexpensive boards can run micropython. The problem was that I wasn't able to load any code on the board. The Python REPL worked, but when the board was restarted all the code typed in was erased. This brought me down the rabbit hole of building custom firmware for the ESP-01 board. 

Getting micropython onto the little ESP-01 board with only 512 kB of flash memory was really cool. It is amazing that such a small, cheap piece of hardware car run Python. The problem was that if I want to turn the ESP-01 into something useful, it has to have a Python program running on it. The REPL worked great. But when I tried to use ampy to upload a .py file onto it, the terminal just spit out an error. After watching a couple YouTube videos on pushing micropython to adafruit boards, I thing the only way to get a .py file on the ESP-01 is to have the .py file baked into the firmware. How hard can that be? Pretty hard actually. Building custom firmware is kind of a daunting task. Here's how I finally got it to work.

Summary of Steps:

1. Go to the den and use the Linux Desktop running Ubuntu 16.04
2. Download losts of dependancies
3. Mess around with the ESP SDK
4. Clone the micropython repo and build the firmware


### 1. Go to the den and use the Linux Desktop running Ubuntu 16.04

I initially tried to building the micropython firmare for the ESP-01 board in a Virtual Machine running on a Windows 10 laptop. A Virtual Machine is like a computer running inside another computer. The Virtual Machine was created using Vagrant. Getting the VM up and running went fine. Cloning the github repo inside the VM worked great. But building the ESP SDK just wouldn't work. I kept getting errors and the build never completed. I have an actual linux computer in the den, so after messing around with the VM for a couple hours, I decided to just use an actual Ubuntu 16.04 box. 



### 2. Install lots of dependancies

In order to build the micropython firmware for the ESP-01, we need toinstall a bunch of dependancies 

### 3. A neat burried function in the Micropython Firmware

I couldn't figure out how much flash memory my little ESP-01 board had. I assumed they had 512 kB of flash memory. After having trouble building the special 512 kB firmware, and having no luck, I accidentally uploaded the full micropython firmware (the firmware designed for 4 MB flash modules like the ESP-12 on the Adafruit Feather Huzzah) on the little ESP-01 board. But the large firware file uploaded fine, and the REPL started and worked. Huh... I though that the full size firmware wouldn't fit on the little ESP-01 board, but it actually did. I was digging through my `~/micropython/ports/esp8266/modules` directory and tried a couple different module imports

```
>>> import ntptime
>>> dir(ntptime)
>>> import dht
>>> dir(dht)
```

All of the modules imported fine on the little ESP-01 board. There was one .py file in the module folder called ```port_diag.py``` The output from the import was pretty interesting:

```
>>> import port_diag
All the stuff


```

It looks like my little ESP-01 boards actually have 1 MB of flash memory, not 512 kB, as I assumed. Great! This means that the full micropython firmware will fit. THe  ```import port_diag``` call also shows how big the firmware file is. For my custom firmware, the total was 578255. I think that means 578225 bytes which is 578 kB or a little over half a MB. With 1 MB of flash memory on my little ESP-01 board, that's over half of the flash memory taken up. But it the full firmware does actually run and upload.

So now the next task will be paring down the firmware build so that we still have the full micropython firmware, but leave out the modules we don't need (like the temperature sensor or Neopixel modules) and put in some custom modules we do want like a WiFi tools module and a ThingSpeak.com module. I want to make sure there is enough room left for the regular micropython file system, because I want to upload a main.py file using ampy that will run on the little ESP-01 board as soon as it powers up. I'm also going to have to figure out a way to parse the junk that comes out when I do an http GET request from ThingSpeak. There is a lot of header junk that I don't want.

Save those for next time...