Title: Building Micropython Firmware for Two Dollar ESP8266-01 Modules
Date: 2018-07-29 09:01
Modified: 2018-07-29 09:01
Status: Draft
Category: micropython
Tags: python, micropython, esp8266, microcontroller, firmware
Slug: building-mircopython-firmware
Authors: Peter D. Kazarinoff
Series: micropython
series_index: 8
Summary: This is the eighth part of a multipart series on Micropython. In this last post of the series, we uploaded Micropython on a cheap $3 ESP8266-01 board. In this post, we will journey down the rabbit hole of building custom firmware for the ESP-01 boards. 

This is the eighth part of a multipart series on Micropython. In this last post of the series, we will uploaded Micropython on a cheap $3 ESP8266-01 board with only 1 MB of flash memory. It is pretty amazing that even these inexpensive boards can run Micropython. Although the small ESP-01 can run Micropython, The problem is I wasn't able to load any code (upload any **_.py_** files) onto little ESP-01 board. The Micropython REPL worked, but when the board was unplugged then restarted, all the code typed into the REPL was erased. This brought me down the rabbit hole of building custom Micropython firmware for the ESP-01 board. 

Getting Micropython onto the little ESP-01 board with only 1 MB of flash memory was really cool. It is amazing that such a small, cheap piece of hardware can run Python. The problem is that if I want to turn the ESP-01 into something useful, it has to have a Python program running on the little board. The REPL worked great. But when I tried to use **ampy** to upload a **_.py_** file onto it, the terminal just spit out an error. After watching a couple YouTube videos on pushing Micropython to Adafruit boards, I think the only way to get a **_.py_** file on the ESP-01 is to have the **_.py_** file baked into the firmware.

 > How hard can that be? Pretty hard actually. Building custom firmware is kind of a daunting task. Here's how I finally got it to work.

Summary of Steps:

1. Go to the den and use the Linux Desktop running Ubuntu 16.04
2. Install the ESP Open SDK
3. Build the Micropython firmware
4. Upload the firmware to the ESP-01
5. Test out the Micropython REPL
6. A neat buried function in the Micropython firmware

### 1. Go to the den and use the Linux Desktop running Ubuntu 16.04

I initially tried to building the Micropython firmware for the ESP-01 board in a Virtual Machine (a VM) running on a Windows 10 laptop. A Virtual Machine is like a computer running inside another computer. The Virtual Machine was created using Vagrant. Getting the VM up and running went fine. Cloning the github repo inside the VM worked great. But building the ESP SDK just wouldn't work. I kept getting errors and the build never completed. I have an actual Linux computer running Ubuntu 16.04 in my den, so after messing around with the VM running in Windows 10 for a couple hours, I decided to just use an actual Linux computer.

### 2. Install the ESP Open SDK

In order to build the Micropython firmware for the ESP-01. First I needed to build and install the ESP Open SDK. 

According to the [Micropython docs](https://github.com/micropython/micropython/tree/master/ports/esp8266):

 > The tool chain required for the build is the OpenSource ESP SDK, which can be found at [https://github.com/pfalcon/esp-open-sdk](https://github.com/pfalcon/esp-open-sdk). Clone this repository and run make in its directory to build and install the SDK locally. Make sure to add toolchain bin directory to your PATH. Read esp-open-sdk's README for additional important information on toolchain setup.
 
Over on pfalcon's [esp-open-sdk github repo README](https://github.com/micropython/micropython/tree/master/ports/esp8266), a bunch of dependencies need to be installed first before building the ESP SDK.

```bash
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install make unrar-free autoconf automake libtool gcc g++ gperf 
$ sudo apt-get install flex bison texinfo gawk ncurses-dev libexpat-dev python-dev python python-serial
$ sudo apt-get install sed git unzip bash help2man wget bzip2 libtool-bin autoconf gperf help2man libtool libtool.bin
```

Next step was cloning the esp-open-sdk repo and running the ```make``` command. I went through a bunch of times trying to run the ```make``` command without success. Each time an error popped up, I looked to see if there was some package missing that could be installed with ```apt-get install```. Eventually with all the needed packages installed, the ```make``` command ran. The build process took a long time. Over 10 minutes.

```bash
$ git clone --recursive https://github.com/pfalcon/esp-open-sdk.git
$ cd esp-open-sdk
$ make
```

pfalcon notes that the ```xtensa-lx106-elf/bin/``` subdirectory needs to be added to your PATH.

 > Once you complete build process as described above, the toolchain (with the Xtensa HAL library) will be available in the xtensa-lx106-elf/ subdirectory. Add xtensa-lx106-elf/bin/ subdirectory to your PATH environment variable to execute xtensa-lx106-elf-gcc and other tools. 

Of the differences between Linux and Windows, the one I still have trouble wrapping my head around is messing around with PATH. Each time I need to modify PATH or make something executable from the command line, I have to hit up google and stack overflow. To add the xtensa subdirectory PATH, I used the following commands:

```bash
$ echo 'export PATH=$PATH:/home/peter/esp-open-sdk/xtensa-lx106-elf/bin/' >> ~/.bashrc
$ source ~/.bashrc
```

### 3. Build the Micropython firmware

With the esp-open-sdk installed, it's time to clone the main Micropython repo and build the ESP8266 firmware. Some more terminal commands did the trick.

```bash
$ cd ~
$ git clone git@github.com:micropython/micropython.git
$ cd micropython
$ git submodule update --init
``` 

Once the whole Micropython repo is cloned locally, the mpy-cross tool needs to be built and then you can jump into the ESP8266 port and build the firmware.

```bash
$ cd ~/micropython
$ make -C mpy-cross
$ cd ports/esp8266
# if building firmware for the second time run $ make clean
$ make
```

According to the Micropython docs, the resulting firmware file will be in the ```/build``` directory.

```bash
$ pwd
~/micropython/ports/esp8266
$ cd build
$ ls
```

The file to look for is **_firmware-combined.bin_**. There will be a lot of files in the build directory, but this is the one we need to upload on the ESP-01 board. 


The full history from the BASH terminal is below:

```text
1961  sudo apt-get install make unrar-free autoconf automake libtool gcc g++ gperf     flex bison texinfo gawk ncurses-dev libexpat-dev python-dev python python-serial     sed git unzip bash help2man wget bzip2
 1962  sudo apt-get install libtool-bin
 1963  git clone --recursive https://github.com/pfalcon/esp-open-sdk.git
 1964  cd esp-open-sdk/
 1965  make
 1966  export PATH=/home/tribilium/esp-open-sdk/xtensa-lx106-elf/bin:$PATH
 1967  source ~/.bashrc
 1968  cd ..
 1969  ls
 1970  cd micropython
 1971  ls
 1972  conda info --envs
 1973  conda activate micropython
 # need to create and activate a Python 2.7 environment with pyserial installed into it
 1974  python
 1975  exit
 1976  ls
 1977  rm -rf micropython/
 1978  ls
 1979  cd ~
 1980  git clone git@github.com:micropython/micropython.git
 1981  git submodule update --init
 1982  cd micropython
 1983  git submodule update --init
 1984  ls
 1985  make -C mpy-cross
 1986  cd ports
 1987  cd esp8266
 1988  make axtls
 1989  make
 1990  cd build
 1991  ls
 1992  cd staticsite
 1993  cd Documents/staticsite
 1994  git add .
 1995  git commit -m "adds"
 1996  git push origin master
 1997  exit
 1998  sudo apt-get update
 1999  sudo apt-get dist-upgrade
 2000  exit
 2001  history
```

### 4. Upload the firmware to the ESP-01

First the ESP-01 needs to be wired up in bootloader mode. Once connected to USB through and FTDI addapter and wired up in bootloader mode the ESP-01 flash can be erased.

```bash
$ esptool.py --port /dev/ttyUSB0 erase_flash
```

With the flash memory erased, the firmware can be uploaded. You need to be in the same directory as the firmware-combined.bin file for the command to work.

```bash
$ cd ~/micropython/ports/esp8266/build
$ esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect 0 firmware-combined.bin
```

### 5. Test out the Micropython REPL

After putting the ESP-01 back into regular running mode, connect the ESP-01 to the Linux computer with the FTDI cable. Try logging in with the screen utility and running a couple commands. The default baud rate that Micropython uses is 115200.

```text
$ screen /dev/ttyUSB0 115200
# [ctrl-c] to reset
>>> import sys
>>> sys.platform
'esp8266'
>>> sys.implementation
(name='micropython', version=(1, 9, 3))
```

### 6. A neat buried function in the Micropython firmware

Initally, I couldn't figure out how much flash memory my little ESP-01 board had. I assumed it had 512 kB of flash memory. After having trouble building the special 512 kB firmware, and having no luck, I accidentally uploaded the full Micropython firmware (the firmware designed for 4 MB flash modules (like the ESP-12 on the Adafruit Feather Huzzah and nodeMCU boards) onto the little ESP-01. But the large firmware file uploaded fine, and the REPL started and worked!? Huh... I though that the full size firmware wouldn't fit on the little ESP-01 board, but it actually did. I was digging through the `~/micropython/ports/esp8266/modules` directory and found a couple **_.py_** files. The **_.py_** files should be built into the firmware. At the Micropython REPL I tried a couple different module imports.

```text
>>> import ntptime
>>> dir(ntptime)
>>> import dht
>>> dir(dht)
```

All of the modules imported fine on the little ESP-01 board. There was one **_.py_** file in the module folder called **_port_diag.py_** The output from the import was pretty interesting:

```text
>>> import port_diag
#All the stuff
```

It looks like my little ESP-01 board actually has 1 MB of flash memory, not 512 kB, as I assumed. Great! This means that the full Micropython firmware will fit. The  ```import port_diag``` call also shows how big the firmware file is. For my custom firmware, the total was 578255. I think that means 578225 bytes which is 578 kB or a little over half a MB. With 1 MB of flash memory on my little ESP-01 board, that's over half of the flash memory taken up. But it the full firmware does actually upload and run.

So now the next task will be paring down the firmware build so that we still have the full Micropython firmware, but leave out the modules we don't need (like the temperature sensor or Neopixel modules) and put in some custom modules we do want like a WiFi tools module and a ThingSpeak.com module. This should be as simple as modifying which files are in `~/micropython/ports/esp8266/modules` and running ```$ make clean``` and ```$ make``` to output a custom firmware **_.bin_** file. Any **_.py_** file in the ```/modules``` subdirectory will make it into the firmware when it gets built.

I also want to make sure there is enough room left for the regular Micropython file system, because I want to upload a main.py file using **ampy** that will run on the little ESP-01 board as soon as it powers up. I'm also going to have to figure out a way to parse the junk that comes out when I do an http GET request from ThingSpeak. There is a lot of header junk that I don't want.

Save those for next time...