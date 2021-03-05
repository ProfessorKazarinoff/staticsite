Title: How to put MicroPython on an ESP8266 microcontroller
Date: 2021-04-04 09:01
Modified: 2021-04-04 09:01
Status: draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller
Slug: how-to-put-micropython-on-an-esp8266
Authors: Peter D. Kazarinoff

[![micropython and esp8266]({static}/posts/micropython/images/fritzing_esp8266.png)]({filename}/posts/micropython/how-to-put-micropython-on-an-esp8266.md)

In this post, you'll learn how to put MicroPython on an ESP8266 microcontroller. [Micropython](http://micropython.org/) is a port, or version of Python designed to run on small, inexpensive, low-power microcontrollers. Examples of microcontrollers that Micropython can run on include the [pyboard](https://store.micropython.org/), the [WiPy](https://pycom.io/development-boards) and ESP8266 boards like the [Adafruit Feather Huzzah](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266). 

If you want to know more about Micropython, you can read about it in [this post]({filename}/posts/micropython/what_is_micropython.md)

[TOC]

## Prerequisites

To upload Micropython on an ESP8266 microcontroller, you need a couple of things in place:

 * computer with a USB port and internet connection
 * an ESP8266 microcontroller
 * a USB cable to connect the microcontroller to the computer
 * Python installed on your computer

We will install Micropython on our microcontroller with our computer. This computer can be Windows10, MacOS, or Linux. These instructions are written assuming you have a Windows 10 computer, but the same general steps are the same for other operating systems. Your computer needs to be connected to the internet.

You need an ESP8266 microcontroller. There are a couple of different variations. Boards you could use include the [Adafruit Feather Huzzah](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266) and the [HiLetgo ESP8266 NodeMCU CP2102 ESP-12E Development Board](https://www.amazon.com/HiLetgo-Internet-Development-Wireless-Micropython/dp/B081CSJV2V) found on Amazon. This tutorial assumes you have one of these development boards that has a USB port on it, not one of the [small ESP8266 ESP-01 boards](https://www.amazon.com/MakerFocus-Wireless-Transceiver-DC3-0-3-6V-Compatible/dp/B01EA3UJJ4) that only has 6 pins.

You need a USB cable to connect your ESP8266 microcontroller to your computer. Both the Adafruit Feather Huzzah](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266) board and the [HiLetgo ESP8266 NodeMCU](https://www.amazon.com/HiLetgo-Internet-Development-Wireless-Micropython/dp/B081CSJV2V) board use a micro-USB connector. Therefore, you need a micro-USB to USB-A (regular USB) cable. The cable needs to be a USB data cable and not just a USB charging cable. This type of cable is common to many older Android phones and tablets. If you don't have a micro-USB to USB-A cable, you buy them at [Adafruit](https://www.adafruit.com/product/592) and [Amazon](https://www.amazon.com/Amazon-Micro-USB-designed-tablets-readers/dp/B0741WGQ36).

Python needs to be installed on your computer so that you can use **esptool**. I suggest you download and install the [Anaconda distribution of Python](https://anaconda.com/distribution). You can also download Python onto your computer from [Python.org](https://python.org). See [this post]({filename}/posts/installation/installing_anaconda_on_windows.md) to see how to install the Anaconda distribution of Python on Windows.

Now that we have our prerequisites setup, it's time to download the Micropython firmware.

## Download the firmware

The first step to installing Micropython on an ESP8266 microcontroller is to download the Micropython firmware from [Micropython.org](http://micropython.org/).

Click on the [Downloads](https://micropython.org/download/) link.

![micropython downloads page]({static}/posts/micropython/images/micropython_downloads_tab.jpg)

On the downloads page, scroll down the page till you get to the Espressif ESP-based boards section.  

![espressif downloads section]({static}/posts/micropython/images/espressif_section.jpg)

Select the **Generic ESP8266 module**. This brings you to the page containing **Firmware for Generic ESP8266 module**

![firmware for generic esp8266 module page]({static}/posts/micropython/images/firmware_for esp8266_page.jpg)

Select the most recent .bin file. In the picture above, that is ```esp8266-20210202-v1.14.bin```. Click on the link to the .bin file (not on the elf or map link). Save the file to your downloads folder.

![save downloaded .bin file]({static}/posts/micropython/images/save_downloaded_firmware_dialog.jpg)

After the .bin file downloads, you should be able to see it in your downloads folder.

![firmware for generic esp8266 module page]({static}/posts/micropython/images/downloads_folder_in_file_browser.jpg)

Great! We've got the firmware .bin file saved on our computer. To move the firmware onto our ESP8266 microcontroller, we first need to install a package called **esptool**.

## Create a virtual environment and install esptool

Now that the .bin file is download, the next thing we need to do is install a command-line tool called **esptool**. esptool is a Python package that we can run from the command line or terminal to flash our firmware onto our ESP8266 microcontroller. But before we install esptool, let's first create a **virtual environment** for our ESP8266 work. The commands below assume you are using the Anaconda distribution of Python and the Anaconda Prompt for your terminal. Using another terminal and Python's venv module is another option. 

Go to the Windows Start Menu and type ```Anaconda```

![anaconda in windows start menu]({static}/posts/jupyter/anaconda_start_menu.png)

Open the Anaconda prompt and type the command below to create a new virtual environment called ```esp8266```. Note that the ```>``` prompt character doesn't need to be typed. It is included to represent the terminal prompt, not as a character to type.

```text
> conda create -y -n esp8266 python=3.8
```

![firmware for generic esp8266 module page]({static}/posts/micropython/images/conda_create_esp8266_anaconda_prompt.jpg)

After the virtual environment is created, it needs to be activated before we install esptool. Activate the ```esp8266``` virtual environment we just created with the command below. Note that after the activation command is entered, ```(esp8266)``` appears before the prompt. This means the ```esp8266``` virtual environment is active.

```text
> conda activate esp8266
```

![conda activate esp8266]({static}/posts/micropython/images/conda_activate_anaconda_prompt.jpg)

Once the ```esp8266``` environment is activated (you can see ```(esp8266)``` before the prompt), use the command below to install esptool.

```text
> python -m pip install esptool
```

![conda activate esp8266]({static}/posts/micropython/images/pip_install_esptool_anaconda_prompt.jpg)

You can confirm the installation of esptool by typing the command below. The result should be the version of esptool that you installed.

```text
> esptool -h
```

![esptool -h]({static}/posts/micropython/images/esptool_dash_h_anaconda_prompt.jpg)

Now that esptool is installed, we need to install a driver to make sure our computer can recognize our ESP8266 board when we connect it.

## Install the SiLabs driver for the CP210x Chip

Before we can connect our ESP8266 microcontroller to our computer, we need a specific driver installed. For my Windows 10 laptop to see my ESP8266, the [CP210x USB to UART Bridge VCP driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) needs to be downloaded from SiLabs and installed. This is quick and easy but does require admin privileges.

![SiLabs Driver]({static}/posts/micropython/download_silabs_driver.PNG)

Now, we can connect our microcontroller to our computer.

## Connect ESP8266 microcontroller to computer

We've downloaded the firmware .bin file, we've installed esptool using the Anaconda Prompt, and we installed the SiLabs driver. The next step is to connect the ESP8266 microcontroller to the computer. Connect one end of the USB cable to the microcontroller and connect the other end of the cable to a USB port on your computer. Note that **it does make a difference which way is up** for both sides of the USB cable. 

![connect esp8266 to computer]({static}/posts/micropython/images/fritzing_esp8266.png)

## Confirm the ESP8266 is connected and determine the COM#

After the ESP8266 is connected to the computer, you should be able to see the ESP8266 in the Windows Device Manager. You can open the Windows Device Manager from the Windows Start Menu.

![connect esp8266 to computer]({static}/posts/micropython/find_device_manager.png)

In the Windows Device Manager, look in the **Ports (COM & LPT)** section. You should see something like **Silicon Labs CP201x USB to UART Bridge (COM4)**. Make note of which COM# is in parenthesis after UART Bridge. We'll need this COM# in our next step.

![connect esp8266 to computer]({static}/posts/micropython/device_manager_menu.png)

After the ESP8266 is connected to the computer and you know which COM# it corresponds to, you can close the Windows Device Manager and move back to the Anaconda Prompt. It's time to install Micropython on our ESP8266!

## Install Micropython on ESP8266 with esptool

Everything should now be in place. Let's review the steps so far:

 * Downloaded .bin firmware file from the Micropython downloads page
 * Confirmed the .bin file is in our Downloads folder
 * Created a virtual environment using the Anaconda Prompt
 * Activated the virtual environment
 * Installed esptool (into the virtual environment)
 * Confirmed esptool was installed with ```esptool -h```
 * Installed the SiLabs CP210x driver
 * Attached the ESP8266 to the computer with a USB cable
 * Confirmed the ESP8266 was connected in the Windows Device Manager
 * Determined which COM# Port corresponds to the ESP8266

Now the only steps left are to install Micropython on the ESP8266 and confirm that Micropython works. We are almost there.

Go back to the Anaconda Prompt and make sure the ```(esp8266)``` virtual environment is active. Remember in the commands below, you do not need to type ```>```. This ```>``` character is shown to indicate the Anaconda Prompt.

Navigate the Downloads folder:

```text
> cd Downloads
```

You can confirm that you are in the Downloads directory by typing the ```pwd``` command. This will print out the working directory.

```text
> pwd
```

Then type the command below to erase the flash memory on the ESP8266.

```text
> esptool --port COM4 erase_flash
```

![esptool erase flash]({static}/posts/micropython/esptool_erase_flash.PNG)

Now it's time to write the .bin firmware file to the flash memory on the board using the ```esptool write_flash``` command. Make sure to use the exact .bin firmware file name you see sitting in the **Downloads** directory. The port has to be set as the port you found in the Windows Device Manager. ```---baud``` is the baud rate or upload speed. I found that ```--baud 115200``` works just fine. ```--flash_size=detect```means that esptool will figure out how much storage our ESP8266 has. The ```0``` after ```--flash_size=detect``` means we want the firmware to be written at the start of the flash memory (the 0th position) on the board. Again, make sure the .bin firmware file name is correct. It is easy to mistype. The latest version may not be ```esp8266-20210202-v1.14.bin```

```text
> esptool --port COM4 --baud 115200 write_flash --flash_size=detect 0 esp8266-20210202-v1.14.bin
```

![esptool write flash]({static}/posts/micropython/esptool_write_flash.PNG)

Congratulations! Micropython should now be installed on your ESP8266 Microcontroller. To make sure the Micropython installation was successful, we'll connect to the ESP8266 using a tool called PuTTY.

## Download and install PuTTY, a serial monitor

Now that Micropthon is installed on our ESP8266 microcontroller, we can communicate with our ESP8266 over a serial connection. Windows 10 doesn't have a built-in serial monitor (like screen on MacOS and Linux). So we need to download and install **PuTTY**. PuTTY is a lightweight SSH and serial client for Windows. PuTTY allows us to send and receive commands between our computer and our ESP8266 microcontroller. [PuTTY can be downloaded here](https://www.putty.org/). PuTTY is pretty lightweight. The download and installation are pretty quick.

![Download Putty]({static}/posts/micropython/download_putty.PNG)

## Use PuTTY to send commands to the ESP8266

Ensure the ESP8266 board is connected with a USB cable and make sure you can see the ESP8266 in the Windows Device Manager. Then use PuTTY to connect to the board over serial.  Make sure you specify the correct serial port in the **Serial line** box and **115200** baud in the Speed box.

 > **Micropython is set to run at 115200 baud**, other baud rates will lead to junk characters in the serial monitor.
 
You can't connect to the ESP8266 over SSH. You need to select the **Serial** radio button below the header **Connection type:** near the top of the PuTTY window to connect to your ESP8266. 

![PuTTY in start menu]({static}/posts/micropython/putty_in_start_menu.png)

![PuTTY config]({static}/posts/micropython/putty_settings.png)

If you see ```>>>``` the Micropython REPL (the Micropython prompt) is running and the ESP8266 is working! This version of Python isn't running on your computer, it's Micropython running on the little ESP8266 microcontroller! Sometimes you might have to type [Enter] or [Ctrl-D] to get the ```>>>``` REPL prompt to show up. A few times I needed to close PuTTY, unplug then replug the board and try PuTTY again. Many ESP8266 microcontrollers have a tiny little black RESET button that can be pressed to restart the board. If you can't connect to the ESP8266 with PuTTY, you can try pressing the REST button. 

![REPL Prompt]({static}/posts/micropython/REPL_prompt.PNG)

At the ```>>>``` Micropython REPL prompt try the following commands:

```text
>>> print('Micropython for Engineers!')
Micropython for Engineers

>>> import sys
>>> sys.platform
'esp8266'
```

![sys_dot_platform]({static}/posts/micropython/sys_dot_platform.PNG)

## Celebrate!

![party icon]({static}/posts/micropython/images/party_icon.png)

**Let's celebrate! Micropython is running on our ESP8266 microcontroller.**
