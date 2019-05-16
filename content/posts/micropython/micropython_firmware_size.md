Title: Micropython Firmware Size for a 1 MB ESP-01 board
Date: 2018-02-17 09:01
Modified: 2018-02-17 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, firmware
Slug: micropython-firmware-size
Authors: Peter D. Kazarinoff
Series: micropython
series_index:9

This is the ninth part of a multipart series on Micropython. In this last post of the we built custom firmware for the ESP-01 board and found out that the little ESP-01 board had 1MB of flash memory and could fit the full-size firmware version.  In this post we are going to build the new custom firmware that is smaller in size than the full-size version and upload it to the little ESP-01 board 

Summary of Steps:

1. Connect the ESP-01 board and check the firmware "size" and installed modules
2. Look in the modules directory and decide which modules can be removed
3. Rename the modules directory and create a new modules directory with only the necessary modules
4. Build the new smaller-sized firmware
5. Put the ESP-01 board in bootloader mode and flash the new firmware.


### 1. Connect the ESP-01 board and check the firmware "size" and installed modules

Connect the ESP-01 to the serial-USB converter thru the TX, RX and GND pins. Connect the ESP-01 VCC, RST, CHPD and RST pins to 3.3V. Plug the serial-USB converter cable in and turn on the breadboard power supply. Bring up a terminal and open **screen** pointing to the correct port and running at 115200 baud.

```
$ screen /dev/ttyUSB0 115200
```

When the REPL prompt comes up (I had to unplug and replug the serial-USB converter cable once and type Enter to get it to work) type ```help()``` just to make sure micropython is running. Now we can see how big the .bin file was that was uploaded onto the board. There is a "hidden" module in the micropython firmware called **port_diag.py**. You can see it if you go to the micropython repo on github and look in the /ports/esp8266/modules directory. If we import the **port_diag** module from the REPL, we can view the firmware size.

```
>>> import port_diag
```

The output I got was:

```
FlashROM:
Flash ID: 1440e0 (Vendor: e0 Device: 4014)
Flash bootloader data:
Byte @2: 00
Byte @3: 20 (Flash size: 1MB Flash freq: 40MHZ)

Firmware checksum:
size: 579208
md5: e21618fb0232724e69b02b819b8882ca
True

Networking:
STA ifconfig: ('10.0.0.24', '255.255.255.0', '10.0.0.1', '75.75.75.75')
AP ifconfig: ('192.168.4.1', '255.255.255.0', '192.168.4.1', '75.75.75.75')
Free WiFi driver buffers of type:
0: 8 (1,2 TX)>>> dir(ntptime)
1: 0 (4 Mngmt TX(len: 0x41-0x100))
2: 8 (5 Mngmt TX (len: 0-0x40))
3: 4 (7)
4: 7 (8 RX)

Active PCB states:
Listen PCB states:
TIME-WAIT PCB states:
>>>
```

The line I'm looking for is the **size** line. This shows the .bin firmware file size. From the output of **port_diag**, it looks like the .bin file size is:

```
size: 579208 
```

I think this means 579,208 Bytes which is about 579 kB or 0.58 MB. On a 1 MB ESP-01 board, this is over half of the flash memory.

### 2. Look in the modules directory and decide which modules can be removed

When I look in the modules directory of the esp8266 micropython port, I see a couple of files:

```
$ ls ~/micropython/ports/esp8266/modules

apa102.py   flashbdev.py  onewire.py        webrepl.py
_boot.py    inisetup.py   port_diag.py      webrepl_setup.py
dht.py      neopixel.py   upip.py           websocket_helper.py
ds18x20.py  ntptime.py    upip_utarfile.py  wifitools.py
```

I don't need all of these on the little ESP-01 board. So let's see how big each one of these are:

![modules dir]({static}/posts/micropython/micropython_modules.png)

Now to move these to another directory for safe keeping. I built a new directory called modules-orig and copied all the files over. Now it's time to delete all the .py files in the modules directory that we don't need. The only .py files I left were:

```
$ ls
  _boot.py  flashbdev.py  inisetup.py  ntptime.py  port_diag.py  wifitools.py
```

OK, now to build the firmware again. See if anything broke, and see how much space we saved.

```
$ cd ~/micropython/ports/esp8266
$ make clean
$ make
```

Not bad, but not a huge change. After leaving only 6 .py files in the modules folder, the final .bin size was still  562568 B or 0.56 MB. That is only a savings of about 0.02 MB. That really didn't do all that much.
 




