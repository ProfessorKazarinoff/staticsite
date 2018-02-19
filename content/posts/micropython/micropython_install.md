Title: Installing Micropython on an Adadfruit Feather Huzzah ESP8266
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: matplotlib
Tags: python, micropython, esp8266, microcontroller
Slug: micropython-install
Authors: Peter D. Kazarinoff
Series: micropython
series_index:1

This is the first part of a multipart series on Micropython. Micropython is a port of Python that runs on small, inexpensive microcontrollers. In this first post, we will install micropython on an Adafruit Feather Huzzah ESP8266 board using Python and an package called esptool.

To install micropython on a microcontroller, we need the following hardware:

| Hardware | Purpose |
|---|---|
| Windows 10 Laptop | used to download micropython and install |
| Adafruit Feather Huzzah ESP8266 | Microcontroller that will run microphythonn |
| USB Cable | Connect laptop to microcontroller |

To install micropython we will use the following software and tools

| Software | Purpose |
| --- | --- |
| Anaconda distribution of Python on Laptop | Download micropython and install |
| Anaconda Prompt | install esptool using pip |
| esptool.py | a pip installable package that we'll use to install micropython |
| firmware .bin file | the version of micropython that will run on the microcontroller |

Summary of Steps:

1. Install the Anaconda distribution of Python
2. Make a new conda environment and install esptool.py
3. Download the latest micropython firmware .bin file
4. Install the SiLabs driver for the Adafruit Feather Huzzah ESP8266
5. Connect the Adafruit Feather Huzzah ESP8266 board to the laptop
6. Determine the Serial port that the Feather Huzzah is connected to
7. Run the esptool.py to upload the .bin file to the Feather Huzzah
8. Download and install Putty, a serial monitor
9. Use Putty to connect to the Feather Huzzah

### 1. Install the Anaconda distribution of Python

If you don't have Anaconda already installed, go to Anaconda.com/Downloads and install the lastest version.

### 2. Create a new conda environment and install esptool.py

Open the Anaconda prompt and create a new virtual environment

```
conda create -n micropython python=3.6
conda activate micropython
(micropython) cd Documents
(micropython) mkdir micropthon
(micropython) cd micropython
(micropython) pip install esptool
(micropython) conda list
```

### 3. Download the latest micropython firmware .bin file

Go to github and download the latest .bin file. Move the file to the micropython directory

![.bin firmware on github]({filename}/posts/micropython/firmware_download_page.PNG)

### 4. Install the SiLabs driver for the Adafruit Feather Huzzah ESP8266

![SiLabs Driver]({filename}/posts/micropython/download_silabs_driver.PNG)

### 5. Connect the Adafruit Feather Huzzah ESP8266 board to the laptop

Use a microUSB cable to connect the feather huzzah to the computer. Make sure that the microUSB cable is a full USB data cable and not just a simple power cable. 

### 6. Determine the Serial port that the Feather Huzzah is connected to

Use Windows device manager to determine the serial port 

![Find Device Manager]({filename}/posts/micropython/find_device_manager.png)

![Device Manager Menu]({filename}/posts/micropython/device_manager_menu.png)

### 6. Run the esptool.py to upload the .bin file to the Feather Huzzah

Open the Anaconda Prompt and ```cd``` into the directory with the .bin file. Activate the micropython environment. Run ```esptool --help``` to ensure the esptool is installed correctly. 

```
cd Documents
cd micropython
pwd
Documents/micropython
dir
firmware.bin
conda activate micropython
(micropython) esptool. --help
```

![SiLabs Driver]({filename}/posts/micropython/esptool_help.PNG)

First erase what is currently in the flash memory using the ```esptool erease flash``` command. Make sure to specify the ```--port```. In my case this was ```COM4```. Use the port you found active in the Device Manager.

```
(micropython) esptool.py --port COM4 erease flash --baud
```

![esptool erase flash]({filename}/posts/micropython/esptool_erase_flash.PNG)

Then write the .bin file to the flash memory using the ```esptool write``` command. 

```
(micropython) esptool.py --port COM4 write .bin file --baud 
```

![SiLabs Driver]({filename}/posts/micropython/esptool_write_flash.PNG)

### 7. Download and install Putty, a serial monitor

Download and install Putty. Putty is a lightweight ssh and serial terminal for Windows. Putty will allow us to communicate with the Adafruit Feather Huzzah ESP8266.

![Download Putty]({filename}/posts/micropython/download_putty.PNG)

### 8. Use Putty to connect to the Feather Huzzah

Ensure the Feather is connected with a USB cable, and connect with Putty using the proper serial port and 115200 baud.

![Putty in start menu]({filename}/posts/micropython/putty_in_start_menu.png)

![SiLabs Driver]({filename}/posts/micropython/putty_config.PNG)

The Python REPL running on the Adafruit Feather Huzzah ESP8266 will open. This version of Python isn't running on the laptop, it's Python running on the microcontroller!

![SiLabs Driver]({filename}/posts/micropython/REPL_prompt.PNG)

At the command prompt try the following commands

```
>>> print('Micropython for Engineers!')
Micropython for Engineers
```

```
>>> import sys
>>> sys.platform
'esp8266'
```

![SiLabs Driver]({filename}/posts/micropython/sys_dot_platform.PNG)

## Next steps:
Use the Python REPL on the Adafruit Feather Huzzah to blink an LED and read a sensor.