Title: Building an IoT Server with flask and Python - Part 6 - upload code to ESP8266-based WiFi weather stations
Date: 2018-09-11 09:01
Modified: 2018-09-11 09:01
Status: draft
Category: flask
Tags: python, flask, thingspeak, mobile, IoT, sensor
Slug: flask-iot-server-esp8266
Authors: Peter D. Kazarinoff

This is the sixth part of a series of posts about building an Internet of Things (IoT) server with **flask**, Python and ESP8266 microcontrollers. In this post we'll add some code to our ESP8266-based weather stations. The code we upload to the ESP8266's will cause the temperature to be measured. After the ESP8266 measures the temperature it will execute a GET request to our **flask** IoT server web API.

[TOC]

## Introduction

In the last post, we added a database to our **flask** IoT server. Each time our flask IoT server web API is hit with a valid URL, the data contained in the URL is saved as a record in an sqlite3 database on the server. Each time we browse to the main page of the **flask** IoT server site, we see the most recent temperature posted. The posted temperature is pulled from the sqlite3 database. 

In this post we are going to create a couple new **_.py_** files and upload the **_.py_** files to the ESP8266-based WiFi weather stations. These **_.py_** files will enable the the ESP8266-based WiFi weather stations to measure the temperature, then post the temperature to our flask IoT server.

## Hardware Setup

Before we upload any new code to the ESP8266-based weather stations, let's review the hardware setup. Below is a schematic of the ESP8266-based weather stations. The schematic shows an ESP8266 microcontroller (an Adafruit Feather Huzzah ESP8266) connected to a temperature sensor (MCP9808) with jumper wires.

![fritzing sketch]({filename}/posts/micropython/feather_huzzah_temp_sensor_fritzing.png)

## Upload firmware

If you are following along with this series, you might remember the ESP8266-based WiFi weather station hardware and software setup in the first post of the series. In case the Feather Huzzah ESP8266 microcontroller doesn't have an up-to-date version of Micropython on it, below are instructions detailing how to upload the Micropython firmware to the board.

### Download the latest micropython firmware .bin file

Go to github and [download the latest .bin firmware](https://micropython.org/download#esp8266) file. Move the .bin firmware file to a new **micropython** directory. The .bin firmware file is the version of Micropython that will run on the Adafruit Feather Huzzah ESP8266. 

![.bin firmware on github]({filename}/posts/micropython/firmware_download_page.PNG)

### Install the SiLabs driver for the Adafruit Feather Huzzah ESP8266

Before we can connect the Adafruit Feather Huzzah to the computer, we need a specific driver installed. For my Windows 10 laptop to see the Adafruit Feather Huzzah board, the [CP210x USB to UART Bridge VCP driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) needs to be downloaded from SiLabs and installed.

![SiLabs Driver]({filename}/posts/micropython/download_silabs_driver.PNG)

### 5. Connect the Adafruit Feather Huzzah ESP8266 board to the laptop

Use a microUSB cable (the same kind of cable that charges many mobile phones) to connect the Feather Huzzah to the computer. Make sure that the microUSB cable is a full USB __data cable__ and not just a simple power cable. I had trouble getting the Feather Huzzah to work, and it turned out the reason was the micoUSB cable was only a charging cable and could not transfer data. 

### Determine which serial port the Feather Huzzah is connected to

Use Windows Device Manager to determine which serial port the Feather Huzzah board is connected to. We will need the serial port as one of the parameters when we upload the .bin firmware file on the board. Look for something like **Silicon Labs CP210x USB to UART Bridge (COM4)** in the **Ports (COM & LPT)** menu. The USB to UART bridge is actually the Feather Huzzah ESP8266 microcontroller board. CP210x refers to the chip that handles serial communication on the Feather Huzzah, not the esp8266 chip itself. Make note of the number after **(COM )**. It often comes up as **(COM4)** but it may be different on your computer. 

![Find Device Manager]({filename}/posts/micropython/find_device_manager.png)

![Device Manager Menu]({filename}/posts/micropython/device_manager_menu.png)

### Run esptool to upload the .bin file to the Feather Huzzah

Open the Anaconda Prompt and ```cd``` into the  directory with the **_.bin_** firmware file. The **_.bin_** firmware file will be called something like ```esp8266-20171101-v1.9.3.bin```. Activate a new conda virtual environment and install **esptool** into the environment.

```text
> conda create -n micropython python=3.7
> conda activate micropython
> (micropython) pip install esptool
```

Before we write the **_.bin_** firmware file to the ESP8266, we'll first erase the flash memory on the little microcontroller using the ```esptool erase_flash``` command. Make sure to specify the ```--port```. This is the ```COM``` port you found in the Windows Device Manager.  In my case the port was ```COM4```.

```text
> (micropython) esptool --port COM4 erase_flash
```

![esptool erase flash]({filename}/posts/micropython/esptool_erase_flash.PNG)

Now it's time to write the **_.bin_** firmware file to the flash memory on the ESP8266 board using the ```esptool write_flash``` command. Make sure to use the exact **_.bin_** firmware file name. The **_.bin_** firmare filename is easy to mistype. ```--port``` has to be set as the port you found in the Windows Device Manager. ```---baud``` is the baud rate (upload speed). I found that ```--baud 460800``` worked, but you could also specify ```--baud 115200``` which is slower. The upload time was a matter of seconds with either baud rate. The ```0``` after ```--flash_size=dectect``` means we want the firmware to be written at the start of the flash memory (the 0th position) on the board. 

An issue I ran into was that I tried to use the command ```esptool.py``` instead of ```esptool``` as shown on the [Micropython docs](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware). The documentation for [Micropython on the ESP8266](https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware) specifies the command ```esptool.py``` (including the **.py** file extension). This did work on my Windows 10 machine. Omitting the **.py** file extension, and running ```esptool``` worked instead. 

```text
> (micropython) esptool --port COM4 --baud 460800 write_flash --flash_size=detect 0 esp8266-20171101-v1.9.3.bin
```

![esptool write flash]({filename}/posts/micropython/esptool_write_flash.PNG)

## Construct **_run.py_** files

Now that Micropython is loaded on the board, we'll construct a couple of **_.py_** files to load onto the microcontroller.

## Upload the **_.py_** files

We'll use a tool called **ampy** to upload the **_.py_** files to the board. Make sure **ampy** is installed in the virtual environment you're using.

```text
> conda activate micropython
> (micropython) pip install ampy
```

To upload the **_.py_** files, make sure the board is plugged into the computer with a USB data cable and use the **ampy** ```put``` command. Note the ```--port``` is specified.

```text
> (micropython)$ ampy --port COM4 put MCP9808.py
> (micropython)$ ampy --port COM4 put wifitools.py

> (micropython)$ ampy --port COM4 put config.py
> (micropython)$ ampy --port COM4 ls
> boot.py
wifitools.py
MCP9808.py
config.py
```

## Test ESP8266-based weather stations

Use PuTTY to open up the Micropython REPL

```text
>>>
```

## Upload **_main.py_** files

Now that we know our ESP8266-based WiFi weather stations are working correctly, we'll upload a **_main.py_** file to the board that will automatically start recording temperatures and sending the temperature to our flask IoT server web API.

```text
> (micropython) ampy --port COM4 put main.py
> (micropython) ampy --port COM4 ls
wifitools.py
MCP9808.py
config.py
main.py
```

## Summary 

It works! We have a working Internet of Things (IoT) server that has a working web API that ESP8266-based WiFi weather stations can post to.