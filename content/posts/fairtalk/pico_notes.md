Title: Trying out Pico-Notes- a MicroPython web app
Date: 2018-07-18 10:15
Modified: 2018-07-18 10:15
Status: draft
Category: micopython
Tags: python, micropython, ESP8266
Slug: pico-notes-micropython
Authors: Peter D. Kazarinoff
Summary: This post entails my investigation of a micropython project called picoweb. Picoweb is a micropython micro web framework (cute- a pico web framework). In this post, I will run through installing pico web on an ESP8266. 

## What is picoweb

Picoweb is micro web framework that is sort of like flask or bottle. Picoweb runs on smaller microcontrollers with micropython.

## What is pico-notes

Pico-notes is a web app using the picoweb framework. It is a notes app where users can type notes and save them for later.


## Microcontroller vs. Unix distribution of pico-notes

Pico-notes can run on a microcontroller, but there is also a version of Micropython that runs on Unix systems. First we'll try to get the pico-notes running on Unix. Then we will get it pico-notes going on an ESP8266 board.

## Picoweb on Unix

To get picoweb going on Unix, in particular my desktop running Ubuntu 16.04, I first cloned pfalcon's micropython github repository [https://github.com/pfalcon/micropython](https://github.com/pfalcon/micropython). I already cloned the micropython repo, so I used a different directory name for pfalcon's branch. In the pico-notes README, it mentions that running pfalcon's micropython fork is needed to get the application running

 > NOTE: Recent versions of uasyncio async framework and Picoweb web framework, and thus Notes Pico, require "advanced" fork of MicroPython at https://github.com/pfalcon/micropython .

```bash
$ cd ~
$ git clone git@github.com:pfalcon/micropython.git micropython-pfalcon
$ cd micropython-pfalcon
$ git submodule update --init
```

To get the micropython REPL on Ubuntu, you need to ```cd``` into the micropython unix port and run the micropython executable

```bash
$ cd ~/micropython-pfalcon
$ cd ports/unix
$ make axtls
$ make
$ ./micropython
```

When the Micropython REPL comes up, I tested out typical Python commands, then tried some commands that only work in Micropython.

```
MicroPython v1.9.3-902-gd880d5b on 2018-07-18; linux version
Use Ctrl-D to exit, Ctrl-E for paste mode
>>> a = [x**2 for x in range(5)]
>>> print(a)
>>> sys.implementation
(name='micropython', version=(1, 9, 3))
>>> sys.version
'3.4.0'
>>> sys.platform
'linux'
# [ctrl-d] to ext it the REPL
```

Next, I installed pico-notes into the unix version of Micropython with ```upip```

```bash
$ pwd
~/micropython-pfalcon/ports/unix
$ ./micropython -m upip install -p app notes-pico
```

pfalcon notes that that the ```-p app``` flag and argument install notes-pico in the app directory

> app (argument of -p option) is a subdirectory into which to install the application.

Starting pico-notes entails being in the same directory that houses the ```app``` directory assigned above and running Micropython with an environmental variable set.

```
$ MICROPYPATH=app ./micropython -m notes_pico
mem: total=268751, current=62135, peak=76674
stack: 5712 out of 80000
GC: total: 2072832, used: 55712, free: 2017120
 No. of 1-blocks: 551, 2-blocks: 118, max blk sz: 81, max free sz: 62498
* Running on http://127.0.0.1:8081/

# [ctrl-c] to quit
```

Then we can browse on over to [http://127.0.0.1:8081/](http://127.0.0.1:8081/) and see pico-notes in action.

![pico-notes on unix](/posts/fairtalk/pico-notes-on-unix.png)

The app is pretty neat. Type in the text field and click add note. It puts the note below.

![pico-notes on unix](/posts/fairtalk/pico-note-added.png)

After playing around with the notes application, I tried out what it would look like on a phone:

![pico-notes on unix](/posts/fairtalk/pico-note-on-phone.png)

I pulled up a different web browser (chrome) and connected to the same IP address [http://127.0.0.1:8081/](http://127.0.0.1:8081/) with pico-note running. 

![pico-notes on unix](/posts/fairtalk/pico-note-on-chrome.png)

The notes added on chrome were reflected in the notes shown in firefox. Pretty neat!

![pico-notes on unix](/posts/fairtalk/pico-note-back-on-firefox.png)

## picoweb on an ESP8266

Now it is time to build some custom firmware for the ESP8266 because the pico-notes app is too big just to dump as regular .py files, it needs to be built into the firmware that we flash on the ESP8266. This got a little tricky.

First I made sure that I could do a regular build of the Micropython firmware using the official Micropython repository. I pulled down this repo a while ago, but the commands to do it again are:

```bash
$ cd ~
$ git clone git@github.com:micropython/micropython.git
$ git submodule update --init
```

Next, I built the mpy-cross too in the main micropython directory then moved into the exp8266 port and built the firmware.

```bash
$ cd ~/micropython
$ make -C mpy-cross
$ cd ~/micropython/ports/esp8266
$ make axtls
$ make
```

The the make process works, the resulting .bin file shows up in the ```/micropython/ports/esp8266/build``` directory.

```bash
$ cd ~/micropython/ports/esp8266
$ cd build
$ ls
```

There are a lot of files in the directory, but the file we are looking for is named ```firmware-combined.bin```. The micropython docs say that you should erase the flash memory of the ESP8266 before putting on the new firmware. This is done with esptool.

```bash
$ esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py v1.2
Connecting...
Running Cesanta flasher stub...
Erasing flash (this may take a while)...
Erase took 2.6 seconds
```

Now we can put the new firmware onto the ESP8266. I initially had a lot of trouble with this and it came down to an esptool option shown in the micropython docs. My esp8266 board must be a particular NodeMCU board that needs this option:

 > For some boards with a particular FlashROM configuration (e.g. some variants of a NodeMCU board) you may need to use the following command to deploy the firmware (note the -fm dio option):

```bash
$ cd ~/micropython/ports/esp8266/build
$ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 firmware-combined.bin
esptool.py v1.2
Connecting...
Auto-detected Flash size: 32m
Running Cesanta flasher stub...
Flash params set to 0x0240
Writing 581632 @ 0x0... ()1632 (100 %)
Wrote 581632 bytes at 0x0 in 12.7 seconds (367.5 kbit/s)...
Leaving...
```

Now let's try and bring up the Micropython REPL with screen

```text
$ screen /dev/ttyUSBO 115200
# at first nothing, [ctrl-c] brought up the prompt
>>> import sys
>>> sys.platform
'esp8266'
>>> sys.implementation
(name='micropython', version=(1, 9, 3))
>>> import uasyncio
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: no module named 'uasyncio'
```

I have to unplug the ESP8266 in order to get out of screen. So now that the regular micropython build process seems to work, it is time to try the specialized pfalcon build. Note that with the regular esp8266 build, the uasyncio module was not available. 

Next I manually moved all the files that upip downloaded when pico-note was installed on the unix port. These files came from the /micropythonover to the /micropython-pfalcon/ports/esp8266/modules directory. These files came from the ~/micropython-pfalcon/ports/unix/app directory where upip downloaded to. The file list includes:

```text
~/micropython-pfalcon/ports/unix/app/
├── btreedb.py
├── logging.py
├── notes_pico
│   ├── app.py
│   ├── config.py
│   ├── ijson.py
│   ├── __main__.py
│   ├── models_btree.py
│   ├── models_filedb.py
│   ├── models.py
│   ├── models_sqlite.py
│   ├── R.py
│   ├── static
│   ├── templates
│   └── views.py
├── picoweb
│   ├── __init__.py
│   └── utils.py
├── pkg_resources.py
├── uasyncio
│   ├── core.py
│   └── __init__.py
└── utemplate
    ├── compiled.py
    └── source.py
```

These were all moved into the /micropython-pfalcon/ports/esp8266/modules directory, so now it's conents looks like:

```text
.
├── apa102.py
├── _boot.py
├── btreedb.py
├── dht.py
├── ds18x20.py
├── flashbdev.py
├── inisetup.py
├── logging.py
├── neopixel.py
├── notes_pico
│   ├── app.py
│   ├── config.py
│   ├── ijson.py
│   ├── __main__.py
│   ├── models_btree.py
│   ├── models_filedb.py
│   ├── models.py
│   ├── models_sqlite.py
│   ├── R.py
│   ├── static
│   ├── templates
│   └── views.py
├── ntptime.py
├── onewire.py
├── picoweb
│   ├── __init__.py
│   └── utils.py
├── pkg_resources.py
├── port_diag.py
├── uasyncio
│   ├── core.py
│   └── __init__.py
├── upip.py
├── upip_utarfile.py
├── utemplate
│   ├── compiled.py
│   └── source.py
├── webrepl.py
├── webrepl_setup.py
└── websocket_helper.py
```

Then I went into the pfalcon esp8266 port and ran make to build the firmware.

```bash
$ cd ~/micropython-pfalcon
$ cd ports/esp8266
$ make
```

Then I plugged the ESP8266 and ran **esptool** to erase the ESP's flash memory.

```bash
$ esptool.py --port /dev/ttyUSB0 erase_flash
```

With the flash memory erased, now it's time to upload the newly built firmware. The firmware file ends up in /ports/esp8266/build. Again, since I was using some sort of version of the NodeMCU board, I had to include the extra flag

```bash
$ cd ~/micropython-pfalcon
$ cd ports/esp8266/build
$ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect -fm dio 0 firmware-combined.bin
esptool.py v1.2
Connecting...
Auto-detected Flash size: 32m
Running Cesanta flasher stub...
Flash params set to 0x0240
Writing 581632 @ 0x0... ()1632 (100 %)
Wrote 581632 bytes at 0x0 in 12.7 seconds (367.5 kbit/s)...
Leaving...
```

I had some very limited success getting **pico-note** to run on the ESP8266 as an access point. This is the default state that the ESP8266 starts with when loaded with Micropython firmware. I used screen to log into the ESP8226 and start the pico-notes app.

```bash
$ screen /dev/ttyUS0 115200
# [ctrl-c] or reset on ESP8266
>>> import notes_pico.__main__
>>> notes_pico.__main__.main(host="0.0.0.0")
```

Connected to the Micropython Wifi network with a laptop, and used the password micropythoN to join the Wifi network. Pointed a web browser to 192.168.4.1:8081 and tried to use the app. It was very slow and the css didn't load. Many times it timed out. Getting the response back after adding a note showed what looked like json instead of the front facing web app.

Connecting the ESP8266 to the house WiFi worked a lot better. At the micropython REPL on the ESP8266, I stopped the pico-notes app and logged into the house Wifi. Note the IP is different when connected to the house Wifi

```text
# [ctrl-c] to stop process
# [ctrl-d] to restart board
>>> import network
>>> sta_if = network.WLAN(network.STA_IF)
>>> sta_if.active()
False
>>> sta_if.active(True)
>>> sta_if.connect('SSID', 'password')
>>> sta_if.isconnected()
>>> sta_if.ifconfig()
('10.0.0.26', '255.255.255.0', '192.168.0.1', '8.8.8.8')
```

After connected to the house WiFi, I started the pico-note app again

```text
>>> import notes_pico.__main__
>>> notes_pico.__main__.main(host="0.0.0.0")
```

Then I brought my house desktop running Ubunutu over to the ESP's IP address of 10.0.0.26:8081

The pico-note app looked great! I tried adding notes from devices all over the house. Pico-note looked good on the Ubunutu desktop, bad on the Mac Laptop, bad on the Windows laptop, good on two iphones and good on a kindle tablet. For some reason, it looked like the css didn't get loaded on the two laptops.

