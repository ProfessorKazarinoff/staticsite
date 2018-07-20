Title: Micropython on Three Dollar ESP8266-01 Modules
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller
Slug: micropython-on-cheap-modules
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 6

In this post we are going to upload Micropython on a cheap $3 esp8266-01 board with only 1 MB of flash memory. It is pretty amazing that even these inexpensive boards can run Micropython. There are a couple tricks I learned along the way that I wanted to share.

Before we can use upload Micropython to our cheap little board, Python and **esptool** need to be installed on your laptop. I also used a breadboard, an FTDI serial adapter and a breadboard power supply. A little breadboard adapter for the little ESP-01 was also supper helpful. The breadboard adapter and made it easy to break out all of the ESP module's pins which are not breadboard friendly on their own.

Summary of Steps:

1. Hook up ESP-01 in regular running mode (GP0,RST-->3.3V) and test, turn off power
2. Hook up ESP-01 in bootloader mode(GP0->>GND), turn on power, touch RST to ground, then unplug RST
3. Use esptool to write to flash memory
4. Test in putty
5. Wire up LED, test in putty

### 1. Hook up ESP-01 in regular running mode (GP0,RST-->3.3V) and test

Start by hooking up the little ESP-01 board in regular _running mode_. When the ESP-01 is wired up in regular running mode, it can receive commands, run programs, blink LED's etc. This is the way the ESP-01 is usually wired up. Running mode is wired differently than bootloader mode (which we will use later).

Materials:

ESP-01 module: http://a.co/iFkFL7e (the black AI Tinker modules)
breakout boards: http://a.co/8ENtenc
breadboard power supply: http://a.co/6Jxfyfw - wish these had micro usb, not big usb
FTDI serial to microUSB adaptor: http://a.co/j4WGbT3 - wish this could power ESP-01 on it's own. Make sure it is 3.3V capable
Breadboard: various
Jumper Wires: various. Better quality is worth it.

![ESP-01 Regular Run Mode]({filename}/posts/micropython/esp8266_pwr_run_mode_fritzing_sketch_bb.png)

A couple things I learned along the way:

For regular running mode, pins from the ESP-01 need to be connected to:

### ESP-01 Running Mode

| ESP-01 Pin | |
| --- | ---|
| RST | 3.3V |
| GP0 | 3.3V |
| VC  | 3.3V |
| GND | GND  |
| TX  | TX   |
| RX  | RX   |

* Using a breadboard power supply works better than using power from the FTDI adapter. The ESP-01 draws a lot of power
* The FTDI adapter only needs TX, RX and GND connected. Ensure the FTDI adapter is a 3.3V adapter, not a 5V adapter.
* The right angle ESP-01 breakouts are better than the parallel ESP-01 breakouts.
* Putty doesn't seem to work to view AT commands. Needed to use the Arduino IDE serial monitor instead.
* need to get COM Port from the Windows Device Manager

At the Arduino Serial monitor, the following commands should produce output.

```
AT

AT + GMR

AT + RST

```

### 2. Hook up ESP-01 in bootloader mode(GP0 --> GND), turn on power, touch RST to ground, then unplug RST

Afer confirming the ESP-01 can powered up and AT commands can be sent over the Arduino Serial Monitor, it is time to put the ESP-01 in _bootloader mode_. When the ESP-01 is wired up in bootloader mode, firmware can be uploaded to it's flash memory. When the ESP-01 is wired in bootloader mode, it will not run regular commands, blink LED's or run scripts. The ESP-01 bootloader mode is only used when new firmware is uploaded to the board. 

To wire the ESP-01 in bootloader mode:
 
 * Connect GP0 --> GND
 * Power up the ESP-01
 * Touch RST to ground momentarily, then unplug RST.

![ESP-01 Regular Run Mode]({filename}/posts/micropython/ESP-01_bootloader_mode_fritzing_sketch_bb.png)

### ESP-01 Bootloader Mode

| ESP-01 Pin | |
| --- | ---|
| RST | after power, up touch momentarily to GND |
| GP0 | GND |
| VC  | 3.3V |
| GND | GND  |
| TX  | TX   |
| RX  | RX   |



### 3. Use esptool to write to flash memory

With the ESP-01 in bootloader mode, we can upload firmware to the board. But before uploading new firmware, it is a good idea to erase the flash memory on the board.

To erase the ESP-01's flash memory, connect the board to the computer through the FTDI breakout. Power up the board and momentarily touch the RST pin to ground to put the ESP-01 into bootloader mode. Ensure **esptool** is installed in the current virtual environment and run following command at a terminal:

```bash
$ esptool.py --port COM4 erase_flash
``` 

### 3. Use esptool to write to flash memory

With the ESP-01 in bootloader mode, we can upload firmware to the board. But before uploading new firmware, it is a good idea to erase the flash memory on the board.

To erase the ESP-01's flash memory, connect the board to the computer through the FTDI breakout. Power up the board and momentarily touch the RST pin to ground to put the ESP-01 into bootloader mode. Ensure **esptool** is installed in the current virtual environment and run following command at a terminal:

```bash
$ esptool.py --port COM4 erase_flash
``` 

### 4. Upload Micropython firmware

#### Download the latest micropython firmware .bin file

Go to github and [download the latest .bin firmware](https://micropython.org/download#esp8266) file. The .bin firmware file is the version of Micropython that will run on an ESP8266 board. I got the regular version of the ESP8266 firmware (the ESP8266 firmware version that runs on the Adafruit Feather Huzzah and NodeMCU boards) to run on an ESP-01. The version of little ESP-01 board I'm using is from AI Tinker. The little boards are black and have 1MB of flash memory. Some ESP-01 boards have 512 kB of memory and others have 1MB of memory.

![.bin firmware on github]({filename}/posts/micropython/firmware_download_page.PNG)

To upload the firmware to the ESP-01 flash memory, connect the board to the computer through the FTDI breakout. Again, power up the board and momentarily touch the RST pin to ground. This puts the ESP-01 into bootloader mode. Run following command at a terminal, ensure the firmware name corresponds to the firmware you downloaded and that the firware.bin file is in the current working directory:

```bash
$ esptool --port COM4 --baud 115200 write_flash --flash_size=detect 0 esp8266-20171101-v1.9.3.bin
```

### 4. Test in putty

Next we will check the Micropython firmware upload with Putty. Disconnect the ESP-01 from power and wire it up in regular running mode. 

### ESP-01 Running Mode

| ESP-01 Pin | |
| --- | ---|
| RST | 3.3V |
| GP0 | 3.3V |
| VC  | 3.3V |
| GND | GND  |
| TX  | TX   |
| RX  | RX   |

Open a Putty serial terminal session and try the commands:

```text
>>> import sys
>>> sys.implementation
(name='micropython', version=(1, 9, 3))
>>> sys.platform
'esp8266'
```


### 5. Wire up LED, test in putty

Next, we'll see if we can get an LED to blink using the ESP-01 and Micropython. Unplug the ESP-01 from the computer and power. Wire up and LED to GP0 thru a pull up resistor. 

Connect the ESP-01 to the computer and power. Open Putty and try to blink the LED with the commands:

```text
>>> import machine
>>> pin = machine.Pin(0, machine.Pin.OUT)
>>> pin.on()
>>> pin.off()
>>> pin.on()
>>> pin.off()
```

Now let's see if we can blink the LED with a loop:

```text
>>> import time
>>> for i in range(10):
...     pin.on()
...     time.sleep(1)
...     pin.off()
...     time.sleep(1)
...
```


### Conclusion:

It's pretty amazing that Micropython runs on little cheap $3 ESP-01 boards. Although the ESP-01 price is low, there were a couple of pieces of hardware that had to used to get the ESP-01 board to work like a breadboard power supply and an FTDI adapter. If a project used many ESP-01 modules, or size is a big factor in a project,it might make sense to use the cheap little ESP-01 boards. But for my money, I would spend about $5 extra (for a total of only $8) and get one of the ESP8266 NodeMCU boards. These modules have a voltage regulator and FTDI included, plus you get way more GPIO pins to use. It it really cool though to get Micropython running on something so small and cheap as the ESP-01 boards.